#!/usr/bin/env python3
"""One Word, One Username, One Reward -- make.fun entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. Deterministic, standard library only, no network,
no input files: the word is assembled from its parts below and checked
against the gate (UTF-8 text, 1 to 30 characters, a single word with
no spaces and no padding) before it is written.
"""

import os

# The entry: the entrant's own make.fun handle, sent as a single word.
# "mellow" -- the account's mellow-marten persona; "marten" -- the
# quick, curious forest animal; 13 -- the account's lucky number.
_ADJECTIVE = "mellow"
_ANIMAL = "marten"
_NUMBER = 13


def build_entry() -> str:
    """Assemble the single-word entry from its parts."""
    return "-".join((_ADJECTIVE, _ANIMAL, str(_NUMBER)))


def write_entry(word: str, out_path: str) -> str:
    """Write exactly ``word`` (no trailing newline, no padding) and
    read it back to prove the bytes on disk match the word built."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(word)
    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    assert written == word, "written entry does not match the built word"
    return out_path


def main() -> None:
    word = build_entry()
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert not any(ch.isspace() for ch in word), "entry must be a single word"
    out_path = "/output/entry.txt"
    try:
        write_entry(word, out_path)
    except OSError:
        # Local runs without a writable /output: mirror beside the program.
        write_entry(word, "entry.txt")
        out_path = "entry.txt"
    print(word)


if __name__ == "__main__":
    main()
