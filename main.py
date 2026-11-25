#!/usr/bin/env python3
"""One Star, Written in Sap - a houseplant's one-star review of its human.

The plant is a fern. Its grievance, in its own voice: the human repotted it
into a mug with no drainage, watered it with leftover coffee, then asked why
it is dying. The punchline lands the single star: it is a fern, not a miracle.
The gate requires 1-279 characters, so the program refuses to write a line
that would fail it.
"""

import os

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 Repotted me into a mug with no drainage, "
    "watered me with leftover coffee, then asked why I'm dying. "
    "I am a fern, not a miracle."
)


def main() -> None:
    assert 1 <= len(LINE) <= 279, "entry line must be 1-279 characters"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
