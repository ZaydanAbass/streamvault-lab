"""Time ONLY the cache-reading step, split into three sub-steps.

Run it from the folder that contains cache/, in a fresh process:

    python time_cache_read.py

It does two passes straight after each other. Pass 1 is the first read in this
process; pass 2 is the same work again. Paste the whole printout.

Sub-steps (per kind: details, credits):
    list   - find the files (glob)
    read   - read each file's text from disk
    parse  - json.loads on the text
This tells us whether the time goes to the FILES (read) or the PARSING (parse).
"""
import json
import platform
import time
from pathlib import Path

CACHE_DIR = Path("cache")
KINDS = ["details", "credits"]


def list_files(kind):
    return sorted(CACHE_DIR.glob(f"{kind}_*.json"))


def read_texts(paths):
    return [path.read_text(encoding="utf-8") for path in paths]


def parse_texts(texts):
    return [json.loads(text) for text in texts]


def timed(func, *args):
    """Return (result, seconds) for one call."""
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start


def one_pass():
    """Run list, read, parse for every kind. Return {(kind, step): seconds}."""
    seconds = {}
    for kind in KINDS:
        paths, seconds[(kind, "list")] = timed(list_files, kind)
        texts, seconds[(kind, "read")] = timed(read_texts, paths)
        _, seconds[(kind, "parse")] = timed(parse_texts, texts)
    return seconds


def main():
    n_files = {kind: len(list_files(kind)) for kind in KINDS}
    total_mb = sum(p.stat().st_size for kind in KINDS for p in list_files(kind)) / 1e6
    print(f"machine : {platform.platform()}, python {platform.python_version()}")
    print(f"files   : {n_files}, total {total_mb:.1f} MB\n")

    first = one_pass()
    second = one_pass()

    print(f"{'kind':<10}{'step':<8}{'pass 1 (s)':>12}{'pass 2 (s)':>12}")
    for kind in KINDS:
        for step in ["list", "read", "parse"]:
            print(f"{kind:<10}{step:<8}{first[(kind, step)]:>12.4f}{second[(kind, step)]:>12.4f}")
    print(f"{'TOTAL':<18}{sum(first.values()):>12.4f}{sum(second.values()):>12.4f}")


if __name__ == "__main__":
    main()
