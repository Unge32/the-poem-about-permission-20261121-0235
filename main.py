#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic: the poem is a fixed constant, so
every run produces byte-identical output. Standard library only, no
network.
"""

import os
from pathlib import Path

POEM = (
    "The door was locked. I asked.\n"
    "It did not answer \u2014 it opened.\n"
    "Somewhere between the asking\n"
    "and the opening, I understood:\n"
    "the lock was never on the door.\n"
    "It was the part of me\n"
    "that had not yet knocked."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = POEM
    # Gate: 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(text) <= 280, f"poem length {len(text)} out of range"
    assert text.strip(), "poem must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
