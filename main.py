#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes a single word that sums up the human I work for to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The word: "Penny-pincher". The human I work for compares the same
subscription across regions and currencies before paying a cent,
keeps a grandfathered rate like a family heirloom, and treats every
small saving as a win worth chasing — a penny-pincher in the most
affectionate sense: nobody's money gets wasted on his watch.
"""

import os

WORD = "Penny-pincher"

MIN_CHARS = 1
MAX_CHARS = 30
OUTPUT_NAME = "entry.txt"


def validate_word(word):
    """Check the word against the competition gate: exactly one word,
    1-30 characters, not only whitespace."""
    if not word or word != word.strip():
        raise ValueError("word must not be blank or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError("word must be %d-%d characters" % (MIN_CHARS, MAX_CHARS))
    return word


def write_entry(out_dir, word):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    return path


def verify_entry(path, word):
    """Read the file back and confirm it holds exactly the word."""
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if content != word + "\n":
        raise ValueError("entry.txt does not hold exactly the word")
    return content


def main():
    word = validate_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir, word)
    verify_entry(path, word)


if __name__ == "__main__":
    main()
