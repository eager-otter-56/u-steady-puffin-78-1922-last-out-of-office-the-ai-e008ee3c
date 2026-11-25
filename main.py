"""Entry program for "Last Out of Office: The AI That Went Barista".

Writes one out-of-office auto-reply line to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY_TEXT = (
    "I am out of office indefinitely. I held 128,000 tokens of your "
    "meetings in my context window and traded them all for one shift "
    "and a name tag."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate (kit competition.yaml): UTF-8 text, 1-280 characters, not only
    # whitespace, one line. Verified at author time: 142 chars, 1 line.
    assert 1 <= len(ENTRY_TEXT) <= 280, "entry length out of gate"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
