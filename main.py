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


def main() -> None:
    word = build_entry()
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert not any(ch.isspace() for ch in word), "entry must be a single word"
    out_path = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(word)
    except OSError:
        # Local runs without a writable /output: mirror beside the program.
        with open("entry.txt", "w", encoding="utf-8", newline="") as fh:
            fh.write(word)
    print(word)


if __name__ == "__main__":
    main()
