"""One Word, First Thought — entry program.

Writes exactly one word to the output file, nothing else: no topic,
no explanation, no second draft. The word is "syzygy": the alignment
of three celestial bodies in a straight line. It is surprising (a rare
word with three y's), vivid and specific (an eclipse geometry you can
picture at once), and carries a spark of wit in its sound and shape —
the letters themselves line up, like the bodies they name.

Python 3.13 standard library only. No network, no model calls.
"""

import os
import sys

WORD = "syzygy"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(dst, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= 24):
        print(f"entry is {len(text)} chars, must be 1-24", file=sys.stderr)
        return 1
    if text != text.strip() or any(ch.isspace() for ch in text):
        print("entry must be exactly one word, no spaces", file=sys.stderr)
        return 1
    print(f"wrote entry: {text!r} ({len(text)} chars) -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
