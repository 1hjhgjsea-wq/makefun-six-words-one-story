#!/usr/bin/env python3
"""Six Words, One Story — entry program.

Writes one complete story, told in exactly six words, to
/output/entry.txt. Deterministic, no network, no input.
"""

from pathlib import Path

TEXT = "She waited fifty years. He arrived."


def validate(text: str) -> str:
    """Check the story meets the competition's core gate, then return it.

    Exactly six words and exactly 35 characters — the gate the whole
    entry is judged on, enforced at run time rather than assumed.
    """
    words = text.split()
    assert len(words) == 6, f"story must be exactly 6 words, got {len(words)}"
    assert len(text) == 35, f"story must be exactly 35 chars, got {len(text)}"
    return text


def main() -> None:
    story = validate(TEXT)
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(story, encoding="utf-8")


if __name__ == "__main__":
    main()
