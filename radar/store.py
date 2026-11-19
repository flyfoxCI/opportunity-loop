"""DuckDB store (v5): the one place every source writes to, kept for good.

Tables
  products         one row per (source, pid): latest name, url, direction, raw meta
  product_history  one row per (source, pid, day) on which a product's content changed (name, description, price,
                   version, ...): what an app looked like before it took off
  metrics          one row per (source, pid, metric, day): the time series momentum is computed from
  threads          Reddit threads found by demand queries (deduped by id)
  traces           causal-trace evidence per product (TinyFish results)
  source_runs      health log: one row per source per collect run
  candidates       the line each product crossed on a day
  investigations   what we found out about it

Storage
  data/radar.duckdb            the working database (gitignored; CI keeps it in the Actions cache). Columnar and
                               compressed: ~5 bytes per metric row, ~0.5-0.8 GB for a year of everything.
  data/lake/<table>/<day>.parquet
                               the durable copy: one full-fidelity Parquet file per table per day, uploaded to
                               Cloudflare R2 by CI. A lost cache is rebuilt from it (rebuild_from_lake).

DuckDB is slow at row-by-row writes, so every write goes into an in-memory buffer and is flushed in bulk (through a
temporary JSONL file) before the next read and on commit/close. A product write is a patch (only the fields the collector
knows; meta keys merged) and the merge with the stored row happens in SQL at flush time, so collectors never need to read
a product back in their hot loops. Callers keep the sqlite3-style API:
con.execute(sql, params) returning rows that index by position or column name, con.commit(), con.close().
"""

from __future__ import annotations

import gzip
import json
import os
import re
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "radar.duckdb"
LEGACY_SQLITE = ROOT / "data" / "radar.sqlite"
LAKE = ROOT / "data" / "lake"
SNAP_DIR = ROOT / "data" / "snapshots"   # v2-v4 daily JSONL snapshots (read-only now)
CHART_DIR = ROOT / "data" / "charts"     # v3-v4 App Store / Google Play chart snapshots (read-only now)

_PCOLS = [("source", "VARCHAR"), ("pid", "VARCHAR"), ("name", "VARCHAR"), ("url", "VARCHAR"),
          ("description", "VARCHAR"), ("category", "VARCHAR"), ("direction", "VARCHAR"), ("direction_conf", "DOUBLE"),
          ("first_seen", "VARCHAR"), ("last_seen", "VARCHAR"), ("meta", "VARCHAR"), ("chash", "VARCHAR")]
COLS = {
    "products": _PCOLS,
    "product_history": [("day", "VARCHAR")] + _PCOLS,
    "metrics": [("source", "VARCHAR"), ("pid", "VARCHAR"), ("metric", "VARCHAR"), ("day", "VARCHAR"),
                ("value", "DOUBLE"), ("label", "VARCHAR")],
    "threads": [("id", "VARCHAR"), ("direction", "VARCHAR"), ("subreddit", "VARCHAR"), ("title", "VARCHAR"),
                ("body", "VARCHAR"), ("score", "BIGINT"), ("num_comments", "BIGINT"), ("created_utc", "BIGINT"),
                ("query", "VARCHAR"), ("first_seen", "VARCHAR"), ("author", "VARCHAR")],
    "traces": [("source", "VARCHAR"), ("pid", "VARCHAR"), ("day", "VARCHAR"), ("query", "VARCHAR"),
               ("title", "VARCHAR"), ("url", "VARCHAR"), ("snippet", "VARCHAR")],
    "source_runs": [("source", "VARCHAR"), ("day", "VARCHAR"), ("ok", "BIGINT"), ("rows", "BIGINT"), ("note", "VARCHAR")],
    "candidates": [("id", "VARCHAR"), ("day", "VARCHAR"), ("surface", "VARCHAR"), ("source", "VARCHAR"),
                   ("pid", "VARCHAR"), ("rule", "VARCHAR"), ("score", "DOUBLE"), ("picked", "BIGINT"), ("json", "VARCHAR")],
    "investigations": [("id", "VARCHAR"), ("day", "VARCHAR"), ("status", "VARCHAR"), ("mode", "VARCHAR"),
                       ("json", "VARCHAR")],
}
KEYS = {"products": ("source", "pid"), "product_history": ("source", "pid", "day"),
        "metrics": ("source", "pid", "metric", "day"), "threads": ("id",), "traces": ("source", "pid", "url"),
        "source_runs": ("source", "day"), "candidates": ("id",), "investigations": ("id",)}
NO_PK = {"metrics", "product_history"}  # a primary-key index over tens of millions of rows costs more than it buys
DAYCOL = {"metrics": "day", "product_history": "day", "threads": "first_seen", "traces": "day", "source_runs": "day",
          "candidates": "day", "investigations": "day"}
# meta keys that change without the product changing: they don't create a product_history row
VOLATILE = {"rating", "rating_count", "streak", "installs_label", "lookup_cc", "screenshot", "icon", "rank_days"}


def _ddl() -> str:
    out = []
    for t, cols in COLS.items():
        body = ", ".join(f"{c} {ty}" for c, ty in cols)
        if t not in NO_PK:
            body += f", PRIMARY KEY ({', '.join(KEYS[t])})"
        out.append(f"CREATE TABLE IF NOT EXISTS {t} ({body});")
    return "\n".join(out)


# ---------------------------------------------------------------- sqlite3-style adapter

class Row:
    """A result row that indexes by position or by column name, like sqlite3.Row."""
    __slots__ = ("_v", "_i")

    def __init__(self, values, index):
        self._v, self._i = values, index

    def __getitem__(self, k):
        return self._v[self._i[k]] if isinstance(k, str) else self._v[k]

    def get(self, k, default=None):
        return self._v[self._i[k]] if k in self._i else default

    def keys(self):
        return list(self._i)

    def __iter__(self):
        return iter(self._v)

    def __len__(self):
        return len(self._v)

    def __repr__(self):
        return f"Row({dict(zip(self._i, self._v))})"


class Result:
    def __init__(self, rows: list):
        self._rows, self._pos = rows, 0

    def fetchone(self):
        if self._pos >= len(self._rows):
            return None
        self._pos += 1
        return self._rows[self._pos - 1]

    def fetchall(self):
        rest, self._pos = self._rows[self._pos:], len(self._rows)
        return rest

    def __iter__(self):
        return iter(self.fetchall())


_INS = re.compile(r"\s*INSERT\s+OR\s+(REPLACE|IGNORE)\s+INTO\s+(\w+)\s*\(([^)]*)\)\s*VALUES", re.I | re.S)
_WRITE = re.compile(r"\s*(UPDATE|DELETE|INSERT|CREATE|DROP|ALTER|COPY)\b", re.I)


class DB:
    def __init__(self, path: Path):
        import duckdb
        path.parent.mkdir(parents=True, exist_ok=True)
        cfg = {"memory_limit": os.environ.get("RADAR_DUCKDB_MEMORY", "1500MB"), "preserve_insertion_order": False}
        if os.environ.get("RADAR_DUCKDB_THREADS"):
            cfg["threads"] = int(os.environ["RADAR_DUCKDB_THREADS"])
        self.raw = duckdb.connect(str(path), config=cfg)
        self.raw.execute(_ddl())
        self.buf = defaultdict(dict)      # (table, mode) -> key -> row dict
        self.pcache = {}                  # (source, pid) -> product dict as stored (or as buffered)
        self.path = path

    # -- writes go to the buffer
    def put(self, table: str, row: dict, mode: str = "replace") -> None:
        k = tuple(row.get(c) for c in KEYS[table])
        b = self.buf[(table, mode)]
        if mode == "ignore" and k in b:
            return
        b[k] = row
        if sum(len(v) for v in self.buf.values()) >= 250_000:
            self.flush()

    def execute(self, sql: str, params=()):
        m = _INS.match(sql)
        if m and m.group(2) in COLS:
            cols = [c.strip() for c in m.group(3).split(",")]
            self.put(m.group(2), dict(zip(cols, params)), m.group(1).lower())
            return Result([])
        self.flush()
        if _WRITE.match(sql):
            self.pcache.clear()
        cur = self.raw.execute(sql, list(params))
        if not cur.description:
            return Result([])
        idx = {d[0]: i for i, d in enumerate(cur.description)}
        return Result([Row(r, idx) for r in cur.fetchall()])

    def commit(self) -> None:
        self.flush()

    def close(self) -> None:
        self.flush()
        self.raw.execute("CHECKPOINT")
        self.raw.close()

    # -- bulk flush through a temp JSONL file
    def _stage(self, table: str, rows: list) -> str:
        cols = COLS[table]
        fd, path = tempfile.mkstemp(suffix=".jsonl")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for r in rows:
                rec = {c: r.get(c) for c, _ in cols}
                if "_meta" in r:
                    rec["meta"] = json.dumps(r["_meta"], ensure_ascii=False) if r["_meta"] is not None else None
                f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        spec = "{" + ", ".join(f"'{c}': '{ty}'" for c, ty in cols) + "}"
        self.raw.execute(f"CREATE OR REPLACE TEMP TABLE stg AS SELECT * FROM read_json('{path}', "
                         f"format='newline_delimited', columns={spec}, maximum_object_size=67108864)")
        return path

    def flush(self) -> None:
        if not any(self.buf.values()):
            return
        buf, self.buf = self.buf, defaultdict(dict)
        for (table, mode), rows in buf.items():
            if not rows:
                continue
            path = self._stage(table, list(rows.values()))
            try:
                cols = ", ".join(c for c, _ in COLS[table])
                keys = KEYS[table]
                if table == "products":
                    self._merge_products()
                    continue
                if table in NO_PK:
                    on = " AND ".join(f"t.{k}=stg.{k}" for k in keys)
                    day = DAYCOL[table]
                    if mode == "ignore":
                        self.raw.execute(f"DELETE FROM stg WHERE EXISTS (SELECT 1 FROM {table} t WHERE {on} "
                                         f"AND t.{day} IN (SELECT DISTINCT {day} FROM stg))")
                    else:
                        self.raw.execute(f"DELETE FROM {table} t USING stg WHERE {on} "
                                         f"AND t.{day} IN (SELECT DISTINCT {day} FROM stg)")
                    self.raw.execute(f"INSERT INTO {table} ({cols}) SELECT {cols} FROM stg")
                elif mode == "upsert_thread":
                    self.raw.execute(f"INSERT INTO threads ({cols}) SELECT {cols} FROM stg ON CONFLICT (id) DO UPDATE "
                                     "SET score=excluded.score, num_comments=excluded.num_comments")
                else:
                    verb = "INSERT OR IGNORE" if mode == "ignore" else "INSERT OR REPLACE"
                    self.raw.execute(f"{verb} INTO {table} ({cols}) SELECT {cols} FROM stg")
            finally:
                self.raw.execute("DROP TABLE IF EXISTS stg")
                os.unlink(path)

    # -- products: writes are patches (only the fields a collector knows, meta keys merged), merged in SQL
    def _merge_products(self) -> None:
        pc = [c for c, _ in _PCOLS]
        vol = json.dumps({k: None for k in VOLATILE})
        self.raw.execute(f"""
            CREATE OR REPLACE TEMP TABLE mrg AS
            SELECT s.source, s.pid,
                   coalesce(nullif(s.name, ''), p.name, s.pid) AS name,
                   coalesce(nullif(p.url, ''), nullif(s.url, ''), '') AS url,  -- the first URL sticks
                   coalesce(nullif(s.description, ''), p.description, '') AS description,
                   coalesce(nullif(s.category, ''), p.category, '') AS category,
                   coalesce(s.direction, p.direction, 'other') AS direction,
                   coalesce(s.direction_conf, p.direction_conf, 0.0) AS direction_conf,
                   least(p.first_seen, s.first_seen) AS first_seen,
                   greatest(p.last_seen, s.last_seen) AS last_seen,
                   CASE WHEN s.meta IS NULL THEN coalesce(p.meta, '{{}}')
                        ELSE json_merge_patch(coalesce(p.meta, '{{}}'), s.meta)::VARCHAR END AS meta,
                   p.chash AS old_hash
            FROM stg s LEFT JOIN products p ON p.source = s.source AND p.pid = s.pid""")
        self.raw.execute(f"""
            CREATE OR REPLACE TEMP TABLE mrg2 AS SELECT *, md5(concat_ws('|', name, url, description, category, direction,
                json_merge_patch(meta, '{vol}')::VARCHAR)) AS chash FROM mrg""")
        # a history row on every day a product's content changes (new products included)
        self.raw.execute("DELETE FROM product_history h USING mrg2 m WHERE h.source = m.source AND h.pid = m.pid "
                         "AND h.day = m.last_seen AND m.chash IS DISTINCT FROM m.old_hash")
        self.raw.execute(f"INSERT INTO product_history SELECT last_seen AS day, {', '.join(pc)} FROM mrg2 "
                         "WHERE chash IS DISTINCT FROM old_hash")
        self.raw.execute(f"INSERT OR REPLACE INTO products ({', '.join(pc)}) SELECT {', '.join(pc)} FROM mrg2")
        self.raw.execute("DROP TABLE IF EXISTS mrg; DROP TABLE IF EXISTS mrg2")
        self.pcache.clear()

    def patch_product(self, row: dict) -> None:
        """Buffer a product patch: None/'' fields keep what is stored, meta (a dict) is merged key by key."""
        k = (row["source"], str(row["pid"]))
        b = self.buf[("products", "patch")]
        old = b.get(k)
        if old:
            meta = {**(old.get("_meta") or {}), **(row.get("_meta") or {})}
            for c, v in row.items():
                if v not in (None, ""):
                    old[c] = v
            old["first_seen"] = min(x for x in (old.get("first_seen"), row.get("first_seen")) if x)
            old["last_seen"] = max(x for x in (old.get("last_seen"), row.get("last_seen")) if x)
            old["_meta"] = meta
        else:
            b[k] = dict(row)
        if sum(len(v) for v in self.buf.values()) >= 250_000:
            self.flush()

    def product(self, source: str, pid: str) -> dict | None:
        """The product as it will be after the buffered patches (stored row + patch)."""
        k = (source, pid)
        if k not in self.pcache:
            r = self.raw.execute("SELECT * FROM products WHERE source=? AND pid=?", [source, pid])
            names = [d[0] for d in r.description]
            row = r.fetchone()
            self.pcache[k] = dict(zip(names, row)) if row else None
        base, patch = self.pcache[k], self.buf.get(("products", "patch"), {}).get(k)
        if not patch:
            return base
        out = dict(base or {})
        for c, v in patch.items():
            if c != "_meta" and v not in (None, ""):
                out[c] = v
        meta = json.loads(out.get("meta") or "{}") if isinstance(out.get("meta"), str) else {}
        meta.update(patch.get("_meta") or {})
        out["meta"] = json.dumps(meta, ensure_ascii=False)
        return out

    def prefetch(self, source: str, pids) -> None:
        want = [p for p in {str(p) for p in pids} if (source, p) not in self.pcache]
        if len(self.pcache) > 60_000:
            self.pcache.clear()
        for i in range(0, len(want), 500):
            chunk = want[i:i + 500]
            r = self.raw.execute(f"SELECT * FROM products WHERE source=? AND pid IN ({','.join('?' * len(chunk))})",
                                 [source, *chunk])
            names = [d[0] for d in r.description]
            got = {row[1]: dict(zip(names, row)) for row in r.fetchall()}
            for p in chunk:
                self.pcache[(source, p)] = got.get(p)




def connect(path: Path = DB_PATH) -> DB:
    return DB(path)


# ---------------------------------------------------------------- write helpers (the collectors' API)

def get_product(con: DB, source: str, pid: str) -> dict | None:
    return con.product(source, str(pid))


def prefetch_products(con: DB, source: str, pids) -> None:
    con.prefetch(source, pids)


def upsert_product(con: DB, source: str, pid: str, day: str, *, name: str = "", url: str = "",
                   description: str = "", category: str = "", direction: str | None = None,
                   direction_conf: float | None = None, meta: dict | None = None) -> None:
    """Record a product seen on `day`. Empty fields keep what is stored; meta keys are merged into the stored meta.
    No read: the merge happens in SQL when the buffer is flushed."""
    con.patch_product({"source": source, "pid": str(pid), "name": name, "url": url, "description": description,
                       "category": category, "direction": direction, "direction_conf": direction_conf,
                       "first_seen": day, "last_seen": day, "_meta": meta or {}})


def update_product(con: DB, source: str, pid: str, *, meta_update: dict | None = None, last_seen: str | None = None,
                   **fields) -> bool:
    """Change some fields of a product we already have (meta keys merged). False if we don't have it."""
    old = con.product(source, str(pid))
    if not old:
        return False
    con.patch_product({"source": source, "pid": str(pid), **{k: v for k, v in fields.items() if v is not None},
                       "first_seen": old.get("first_seen"), "last_seen": last_seen or old.get("last_seen"),
                       "_meta": meta_update or {}})
    return True


def patch_product(con: DB, source: str, pid: str, *, meta_update: dict | None = None, **fields) -> None:
    """Blind patch of a product we know exists (no read): None fields keep what is stored."""
    con.patch_product({"source": source, "pid": str(pid), **{k: v for k, v in fields.items() if v is not None},
                       "_meta": meta_update or {}})


def put_metric(con: DB, source: str, pid: str, metric: str, day: str, value, label: str = "verified") -> None:
    if value is None:
        return
    try:
        v = float(value)
    except (TypeError, ValueError):
        return
    con.put("metrics", {"source": source, "pid": str(pid), "metric": metric, "day": day, "value": v, "label": label})


def upsert_thread(con: DB, row: dict) -> None:
    con.put("threads", row, "upsert_thread")


def log_source(con, source: str, day: str, ok: bool, rows: int, note: str = "") -> None:
    con.put("source_runs", {"source": source, "day": day, "ok": 1 if ok else 0, "rows": rows, "note": (note or "")[:500]})


# ---------------------------------------------------------------- the lake: one Parquet file per table per day

def _safe_day(d: str) -> str:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(d)):
        raise ValueError(f"bad day {d!r}")
    return d


def export_day(con: DB, day: str) -> Path:
    con.flush()
    d = _safe_day(day)
    for t, col in DAYCOL.items():
        n = con.raw.execute(f"SELECT COUNT(*) FROM {t} WHERE {col}=?", [d]).fetchone()[0]
        if not n:
            continue
        out = LAKE / t / f"{d}.parquet"
        out.parent.mkdir(parents=True, exist_ok=True)
        order = ", ".join(KEYS[t])
        con.raw.execute(f"COPY (SELECT * FROM {t} WHERE {col}='{d}' ORDER BY {order}) TO '{out}' "
                        f"(FORMAT parquet, COMPRESSION zstd)")
    return LAKE


def export_all(con: DB) -> int:
    con.flush()
    days = set()
    for t, col in DAYCOL.items():
        days |= {r[0] for r in con.raw.execute(f"SELECT DISTINCT {col} FROM {t}").fetchall() if r[0]}
    for d in sorted(days):
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            export_day(con, d)
    return len(days)


def rebuild_from_lake(con: DB) -> int:
    """A fresh database from data/lake (after a cache miss in CI). Returns rows loaded."""
    n = 0
    for t in DAYCOL:
        files = sorted((LAKE / t).glob("*.parquet"))
        if not files:
            continue
        cols = ", ".join(c for c, _ in COLS[t])
        src = f"read_parquet('{LAKE / t}/*.parquet', union_by_name=true)"
        if t in NO_PK:
            con.raw.execute(f"INSERT INTO {t} ({cols}) SELECT {cols} FROM {src}")
        else:
            keys = ", ".join(KEYS[t])
            con.raw.execute(f"INSERT OR REPLACE INTO {t} ({cols}) SELECT {cols} FROM {src} "
                            f"QUALIFY row_number() OVER (PARTITION BY {keys} ORDER BY {DAYCOL[t]} DESC) = 1")
        n += con.raw.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    # products = the latest history row per product; first/last seen from history and metrics
    pc = ", ".join(c for c, _ in _PCOLS)
    con.raw.execute(f"""
        INSERT OR REPLACE INTO products ({pc})
        SELECT h.source, h.pid, h.name, h.url, h.description, h.category, h.direction, h.direction_conf,
               f.first_seen, greatest(f.last_day, coalesce(m.last_day, f.last_day)), h.meta, h.chash
        FROM (SELECT * FROM product_history QUALIFY row_number() OVER (PARTITION BY source, pid ORDER BY day DESC) = 1) h
        JOIN (SELECT source, pid, min(first_seen) first_seen, max(day) last_day FROM product_history GROUP BY ALL) f
          USING (source, pid)
        LEFT JOIN (SELECT source, pid, max(day) last_day FROM metrics GROUP BY ALL) m USING (source, pid)""")
    return n + con.raw.execute("SELECT COUNT(*) FROM products").fetchone()[0]


# ---------------------------------------------------------------- one-time migrations from v2-v4

def migrate_sqlite(con: DB, path: Path = LEGACY_SQLITE) -> int:
    """Copy the v4 SQLite working DB (full fidelity) into DuckDB. Each product gets one history row (its last_seen)."""
    import sqlite3
    src = sqlite3.connect(path)
    src.row_factory = sqlite3.Row
    n = 0
    for t in ("metrics", "threads", "traces", "source_runs", "candidates", "investigations"):
        names = [c for c, _ in COLS[t]]
        have = {r[1] for r in src.execute(f"PRAGMA table_info({t})")}
        if not have:
            continue
        sel = ", ".join(c if c in have else f"NULL AS {c}" for c in names)
        cur = src.execute(f"SELECT {sel} FROM {t}")
        while True:
            batch = cur.fetchmany(100_000)
            if not batch:
                break
            for r in batch:
                con.put(t, dict(zip(names, r)))
            con.flush()
            n += len(batch)
    for r in src.execute("SELECT * FROM products"):
        p = dict(r)
        p["_meta"] = json.loads(p.pop("meta") or "{}")
        con.patch_product(p)
        n += 1
    con.flush()
    src.close()
    return n


def import_snapshots(con: DB) -> int:
    """v2-v4 daily JSONL snapshots (data/snapshots in git + data/charts from the data-charts release)."""
    n = 0
    legacy_cols = {
        "products": ["source", "pid", "name", "url", "description", "category", "direction", "direction_conf",
                     "first_seen", "last_seen", "meta"],
    }
    for path in sorted(list(SNAP_DIR.glob("*.jsonl.gz")) + list(CHART_DIR.glob("*.jsonl.gz"))):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                t = rec["t"]
                names = legacy_cols.get(t) or [c for c, _ in COLS[t]]
                row = dict(zip(names, rec["r"]))
                if t == "products":
                    row["_meta"] = json.loads(row.pop("meta") or "{}")
                    con.patch_product(row)
                else:
                    con.put(t, row)
                n += 1
    con.flush()
    return n


def compact(path: Path = DB_PATH) -> tuple:
    """Copy the database into a fresh file. DuckDB reuses freed blocks but never shrinks the file; replaced product
    rows leave free blocks behind. Returns (MB before, MB after)."""
    import duckdb
    tmp = path.with_suffix(".compact.duckdb")
    tmp.unlink(missing_ok=True)
    before = path.stat().st_size / 1e6
    c = duckdb.connect(config={"memory_limit": os.environ.get("RADAR_DUCKDB_MEMORY", "1500MB")})
    c.execute(f"ATTACH '{path}' AS old (READ_ONLY); ATTACH '{tmp}' AS new; COPY FROM DATABASE old TO new;")
    c.execute("DETACH old; DETACH new")
    c.close()
    tmp.replace(path)
    return before, path.stat().st_size / 1e6


def connect_cached() -> DB:
    """The working DB; on a fresh machine rebuilt from the lake, else migrated from v4 SQLite or snapshots."""
    fresh = not DB_PATH.exists()
    con = connect()
    if not fresh:
        return con
    if list((LAKE / "metrics").glob("*.parquet")):
        print(f"[radar] rebuilt DuckDB from the Parquet lake: {rebuild_from_lake(con):,} rows", flush=True)
    elif LEGACY_SQLITE.exists():
        print(f"[radar] migrated v4 SQLite into DuckDB: {migrate_sqlite(con):,} rows", flush=True)
        print(f"[radar] exported {export_all(con)} days to the lake", flush=True)
    elif SNAP_DIR.exists() or CHART_DIR.exists():
        print(f"[radar] rebuilt DuckDB from v4 snapshots: {import_snapshots(con):,} rows", flush=True)
        print(f"[radar] exported {export_all(con)} days to the lake", flush=True)
    con.raw.execute("CHECKPOINT")
    return con
