"""SQLite snapshot store — the one place every source writes to.

Tables
  products   one row per (source, pid): latest name, url, direction, raw meta
  metrics    one row per (source, pid, metric, day): the time series momentum is computed from
  threads    Reddit threads found by demand queries (deduped by id)
  traces     causal-trace evidence per product (TinyFish results)
  source_runs  health log: one row per source per collect run

Every metric row carries an evidence label: verified | estimated | inferred.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "radar.sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
  source TEXT NOT NULL, pid TEXT NOT NULL,
  name TEXT, url TEXT, description TEXT, category TEXT,
  direction TEXT, direction_conf REAL,
  first_seen TEXT, last_seen TEXT, meta TEXT,
  PRIMARY KEY (source, pid)
);
CREATE TABLE IF NOT EXISTS metrics (
  source TEXT NOT NULL, pid TEXT NOT NULL, metric TEXT NOT NULL, day TEXT NOT NULL,
  value REAL, label TEXT NOT NULL DEFAULT 'verified',
  PRIMARY KEY (source, pid, metric, day)
);
CREATE INDEX IF NOT EXISTS metrics_by_metric ON metrics(metric, day);
CREATE TABLE IF NOT EXISTS threads (
  id TEXT PRIMARY KEY, direction TEXT, subreddit TEXT, title TEXT, body TEXT,
  score INTEGER, num_comments INTEGER, created_utc INTEGER, query TEXT, first_seen TEXT, author TEXT
);
CREATE INDEX IF NOT EXISTS threads_by_dir ON threads(direction, created_utc);
CREATE TABLE IF NOT EXISTS traces (
  source TEXT, pid TEXT, day TEXT, query TEXT, title TEXT, url TEXT, snippet TEXT,
  PRIMARY KEY (source, pid, url)
);
CREATE TABLE IF NOT EXISTS source_runs (
  source TEXT, day TEXT, ok INTEGER, rows INTEGER, note TEXT,
  PRIMARY KEY (source, day)
);
"""


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    cols = {r[1] for r in con.execute("PRAGMA table_info(threads)")}
    if "author" not in cols:  # migrate DBs created before the author column
        con.execute("ALTER TABLE threads ADD COLUMN author TEXT")
    return con


def upsert_product(con, source: str, pid: str, day: str, *, name: str = "", url: str = "",
                   description: str = "", category: str = "", direction: str = "other",
                   direction_conf: float = 0.0, meta: dict | None = None) -> None:
    con.execute(
        """INSERT INTO products(source,pid,name,url,description,category,direction,direction_conf,first_seen,last_seen,meta)
           VALUES(?,?,?,?,?,?,?,?,?,?,?)
           ON CONFLICT(source,pid) DO UPDATE SET
             name=excluded.name, url=COALESCE(NULLIF(excluded.url,''),products.url),
             description=COALESCE(NULLIF(excluded.description,''),products.description),
             category=COALESCE(NULLIF(excluded.category,''),products.category),
             direction=excluded.direction, direction_conf=excluded.direction_conf,
             first_seen=MIN(products.first_seen, excluded.first_seen),
             last_seen=MAX(products.last_seen, excluded.last_seen),
             meta=excluded.meta""",
        (source, pid, name, url, description, category, direction, direction_conf, day, day,
         json.dumps(meta or {}, ensure_ascii=False)),
    )


def put_metric(con, source: str, pid: str, metric: str, day: str, value, label: str = "verified") -> None:
    if value is None:
        return
    try:
        v = float(value)
    except (TypeError, ValueError):
        return
    con.execute(
        "INSERT OR REPLACE INTO metrics(source,pid,metric,day,value,label) VALUES(?,?,?,?,?,?)",
        (source, pid, metric, day, v, label),
    )


def log_source(con, source: str, day: str, ok: bool, rows: int, note: str = "") -> None:
    con.execute("INSERT OR REPLACE INTO source_runs(source,day,ok,rows,note) VALUES(?,?,?,?,?)",
                (source, day, 1 if ok else 0, rows, note[:500]))


# ---------------------------------------------------------------- git-friendly snapshots
# The SQLite file is a cache (gitignored). What is committed is one gzip'd JSONL file per day
# under data/snapshots/, so the repo grows by a small append-only file instead of a rewritten
# binary. connect_cached() rebuilds the cache from those files when it is missing.

import gzip  # noqa: E402

SNAP_DIR = ROOT / "data" / "snapshots"
_TABLES = {
    "metrics": ("day", ["source", "pid", "metric", "day", "value", "label"]),
    "products": ("last_seen", ["source", "pid", "name", "url", "description", "category", "direction",
                               "direction_conf", "first_seen", "last_seen", "meta"]),
    "threads": ("first_seen", ["id", "direction", "subreddit", "title", "body", "score", "num_comments",
                               "created_utc", "query", "first_seen", "author"]),
    "traces": ("day", ["source", "pid", "day", "query", "title", "url", "snippet"]),
    "source_runs": ("day", ["source", "day", "ok", "rows", "note"]),
}


def export_day(con, day: str) -> Path:
    SNAP_DIR.mkdir(parents=True, exist_ok=True)
    path = SNAP_DIR / f"{day}.jsonl.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for table, (daycol, cols) in _TABLES.items():
            for r in con.execute(f"SELECT {','.join(cols)} FROM {table} WHERE {daycol}=?", (day,)):
                f.write(json.dumps({"t": table, "r": list(r)}, ensure_ascii=False, separators=(",", ":")) + "\n")
    return path


def export_all(con) -> int:
    days = sorted({r[0] for r in con.execute("SELECT DISTINCT day FROM metrics")} |
                  {r[0] for r in con.execute("SELECT DISTINCT first_seen FROM threads")})
    for d in days:
        export_day(con, d)
    return len(days)


def import_snapshots(con) -> int:
    n = 0
    for path in sorted(SNAP_DIR.glob("*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                cols = _TABLES[rec["t"]][1]
                if rec["t"] == "products":
                    con.execute(
                        f"INSERT INTO products({','.join(cols)}) VALUES({','.join('?' * len(cols))}) "
                        "ON CONFLICT(source,pid) DO UPDATE SET name=excluded.name, url=excluded.url, "
                        "description=excluded.description, category=excluded.category, direction=excluded.direction, "
                        "direction_conf=excluded.direction_conf, first_seen=MIN(products.first_seen, excluded.first_seen), "
                        "last_seen=MAX(products.last_seen, excluded.last_seen), meta=excluded.meta", rec["r"])
                else:
                    con.execute(f"INSERT OR REPLACE INTO {rec['t']}({','.join(cols)}) VALUES({','.join('?' * len(cols))})",
                                rec["r"])
                n += 1
    con.commit()
    return n


def connect_cached() -> sqlite3.Connection:
    fresh = not DB_PATH.exists()
    con = connect()
    if fresh and SNAP_DIR.exists():
        n = import_snapshots(con)
        print(f"[radar] rebuilt cache from snapshots: {n} rows", flush=True)
    return con
