"""The One-Line Laugh entry.

Writes one funny line to /output/entry.txt. Pure standard library.
"""

from pathlib import Path

LINE = (
    "My fitness tracker says I burned 400 calories today, "
    "mostly walking to the fridge to check if I was still hungry."
)

OUTPUT = Path("/output/entry.txt")


def validate(line: str) -> None:
    """Gate guard: the entry must be 1-200 chars, one line, not blank."""
    if not line.strip():
        raise SystemExit("entry is blank")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
