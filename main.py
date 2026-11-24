#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- entry program.

Writes one line -- the error message a kitchen toaster shows its
owner when a bagel gets stuck -- to /output/entry.txt for the judge
to read. Standard library only, no network, no input files,
deterministic output: the same line, the same bytes, every run.
"""

import os

LINE = "ERROR: Your bagel is stuck. It is also, legally, my bagel now."

OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 120 characters, not only
    whitespace, and the brief requires a single short funny line.
    """
    if not 1 <= len(entry) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # bytes written are exactly the 62 characters of the line itself.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
