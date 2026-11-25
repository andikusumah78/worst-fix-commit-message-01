"""Worst Fix Ever: Funniest Commit Message — one commit message for a bug
fix that made everything worse.

The gate accepts UTF-8 text of 1 to 100 characters, not only white space,
so the line is checked here before it is written. The gate runs first in
main(): nothing is written to disk unless the line passes validation, so a
bad line fails loudly instead of producing a bad entry file.
"""

import os

LINE = "fix: end the retry storm — capped retries at zero, the service now fails fast, forever, politely"

def validate_line(line):
    """Gate: one line of UTF-8 text, 1-100 chars, no surrounding whitespace."""
    assert 1 <= len(line) <= 100, "entry must be 1-100 characters"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip() == line, "entry must not start or end with whitespace"


def resolve_out_dir():
    """Return the output directory from MAKEFUN_OUTPUT_DIR, default /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line, out_dir):
    """Write the validated line to entry.txt inside out_dir (UTF-8, no newline)."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


def main():
    validate_line(LINE)
    write_entry(LINE, resolve_out_dir())


if __name__ == "__main__":
    main()
