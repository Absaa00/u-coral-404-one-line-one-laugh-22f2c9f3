#!/usr/bin/env python3
"""One Line, One Laugh — a single funny line, written to /output/entry.txt.

Deterministic: no randomness, no network, no time, no environment input.
The same input always produces the same byte-identical file.
"""

import os

LINE = (
    "My to-do list hired an AI agent \u2014 now even my procrastination "
    "has a project manager and a weekly standup."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert line == LINE.strip(), "the line must have no stray whitespace"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 200 cap"
    assert "\n" not in line, "the entry must be exactly one line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
