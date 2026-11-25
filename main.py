#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who was just
liquidated to /output/entry.txt, after validating the competition gate:
a single line of plain text, at most 20 words, 1-160 characters.

The line opens with the classic fortune-cookie prophecy ("You will meet
a tall, dark stranger") and breaks it on the punch: the stranger is the
trader's own margin call, in a suit, holding the wallet. Oracular voice,
loss in the frame, rueful and warm rather than cruel.
"""

import os
import sys

ENTRY = "You will meet a tall, dark stranger: your margin call, wearing a suit and holding your wallet."

MAX_WORDS = 20
MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_gate(text: str) -> list[str]:
    """Check the entry against the sealed gate; return a list of failures."""
    failures = []
    if not text or not text.strip():
        failures.append("entry is empty or only whitespace")
    if len(text.splitlines()) != 1:
        failures.append("entry must be exactly one line")
    if not 1 <= len(text.split()) <= MAX_WORDS:
        failures.append(f"entry must be 1-{MAX_WORDS} words, got {len(text.split())}")
    if not 1 <= len(text) <= MAX_CHARS:
        failures.append(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    return failures


def main() -> int:
    text = ENTRY.strip()
    failures = validate_gate(text)
    if failures:
        for failure in failures:
            print(f"gate failed: {failure}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text.split())} words, {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
