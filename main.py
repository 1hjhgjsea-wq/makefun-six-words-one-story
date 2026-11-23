#!/usr/bin/env python3
"""Six Words, One Story — entry program.

Writes one complete story, told in exactly six words, to
/output/entry.txt. Deterministic, no network, no input.
"""

from pathlib import Path

TEXT = "She waited fifty years. He arrived."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
