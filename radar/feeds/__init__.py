"""v3 collectors: chart discovery (Appark, Gravity Engine) and store measurement (Google Play, iTunes).

Each module exposes SPEC (what it is, how history works, its evidence label) and a
collect(con, day, cfg) function that writes products + metrics and logs one source_runs row.
The v2 collectors (TrustMRR, Tranco, GitHub, Reddit, TinyFish) still live in radar/sources.py.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request

# A generic browser-like client name: these are public web endpoints, not partner APIs.
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def http(url: str, *, body: dict | None = None, headers: dict | None = None, timeout: int = 30,
         retries: int = 2, pace: float = 0.0, as_json: bool = True):
    """GET (or POST JSON when body is given) with small retry/backoff. Returns parsed JSON or text."""
    data = json.dumps(body).encode() if body is not None else None
    hdrs = {"User-Agent": UA, "Accept": "application/json, text/html;q=0.9, */*;q=0.8"}
    if data is not None:
        hdrs["Content-Type"] = "application/json"
    hdrs.update(headers or {})
    last = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=hdrs), timeout=timeout) as r:
                text = r.read().decode("utf-8", "replace")
            if pace:
                time.sleep(pace)
            return json.loads(text) if as_json else text
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(4 * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            if attempt < retries:
                time.sleep(3 * (attempt + 1))
                continue
            raise
    raise last  # pragma: no cover


def log(msg: str) -> None:
    print(f"[radar] {msg}", flush=True)
