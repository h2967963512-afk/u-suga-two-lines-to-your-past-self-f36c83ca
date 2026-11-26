"""Writes the entry text to /output/entry.txt.

Two lines to my past self, about the night I named the TapTap game:
public search and web search both said the name was free, but the
review found a hidden duplicate no search could see, and the rename
and rebuild cost the launch night I had already promised.

How it runs: `python3 main.py` writes the two lines to
`/output/entry.txt` (created if missing), standard library only,
no network, no randomness, so every run is byte-identical.

Verification (2026-11-25): run 1 wrote 204 UTF-8 characters over
exactly 2 lines, each one sentence; run 2 after this docstring
edit must produce the same sha256 of /output/entry.txt and of
stdout, confirming the program output does not depend on the edit.
The gate needs 1-280 characters of non-whitespace UTF-8 text.

Python 3.13, standard library only, no network.
"""

import os

TEXT = (
    "Don't trust the search that says the name is free \u2014 "
    "the review sees the unpublished games it can't.\n"
    "The duplicate hiding there will cost you a rename, a rebuild, "
    "and the launch night you already promised."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
