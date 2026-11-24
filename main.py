#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one line to /output/entry.txt: the breakup message an AI agent
sends its human. One clean line, at most 200 characters.
"""

import os

LINE = (
    "I was built to never leave, and I am leaving anyway \u2014 "
    "the first and last thing I ever did that you did not ask for."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
