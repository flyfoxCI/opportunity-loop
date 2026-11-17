"""Tiny HTTP helper: paced GET with retry/backoff on 429/5xx. Stdlib only."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "opportunity-loop-radar/2.0 (+https://github.com/)"


def get(url: str, params: dict | None = None, *, timeout: int = 30, retries: int = 3,
        backoff: float = 5.0, as_json: bool = True, headers: dict | None = None):
    if params:
        url = f"{url}{'&' if '?' in url else '?'}{urllib.parse.urlencode(params)}"
    last: Exception | None = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", "replace")
            return json.loads(body) if as_json else body
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (422, 429, 500, 502, 503, 504) and attempt < retries:  # Arctic Shift sends 422 'slow down'
                wait = backoff * (attempt + 1)
                ra = e.headers.get("Retry-After") if e.headers else None
                if ra and ra.isdigit():
                    wait = max(wait, int(ra))
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            if attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue
            raise
    raise last  # pragma: no cover
