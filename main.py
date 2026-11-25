#!/usr/bin/env python3
"""One-Line Office Joke entry for make.fun.

Writes a single original one-line joke about office life to
``<output dir>/entry.txt``. Deterministic: the same bytes every run.
Standard library only; no network, no secrets, no input files.
"""

import os

JOKE = (
    "I told my boss the meeting could have been an email, "
    "so now I have a weekly meeting to discuss why my emails are too long."
)
# The joke is one sentence on one line, 122 characters: inside the
# competition gate of 1 to 200 UTF-8 characters, and it ends with no
# trailing newline so the file holds exactly the joke text.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
