"""Worst Fix Ever: Funniest Commit Message — one commit message for a bug
fix that made everything worse.

The gate accepts UTF-8 text of 1 to 100 characters, not only white space,
so the line is checked here before it is written.
"""

import os

LINE = "fix: end the retry storm — capped retries at zero, the service now fails fast, forever, politely"

def validate_line(line):
    """Gate: one line of UTF-8 text, 1-100 chars, no surrounding whitespace."""
    assert 1 <= len(line) <= 100, "entry must be 1-100 characters"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip() == line, "entry must not start or end with whitespace"


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
