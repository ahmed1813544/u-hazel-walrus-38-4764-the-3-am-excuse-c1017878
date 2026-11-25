#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Stdlib only. Writes one single-line excuse to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""

import os

EXCUSE = (
    "I've signed 41 of your 3 AM ideas and every one is now "
    "a story you tell at brunch as a warning, so no."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only whitespace. The excuse below is one
    # line; the trailing newline keeps it a clean single line.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
