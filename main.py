#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one autocorrect fail (69 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

LINE = "Sorry I'm late, I got stuck in a threesome - I mean traffic. TRAFFIC."


def main() -> int:
    if not (1 <= len(LINE) <= 199):
        raise SystemExit(f"line is {len(LINE)} chars, outside the 1-199 gate")
    if LINE.strip() == "" or "\n" in LINE:
        raise SystemExit("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip guard: the file the grader reads must hold exactly the
    # validated line, byte for byte — refuse a silent partial write.
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            raise SystemExit("entry.txt does not match the validated line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
