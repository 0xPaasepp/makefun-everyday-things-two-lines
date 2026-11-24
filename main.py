#!/usr/bin/env python3
"""Write the two-line entry to /output/entry.txt and print it.

Pure standard library. Deterministic: the same bytes on every run,
from any working directory, with no input, network, or randomness.
"""

import os

ENTRY = (
    "A traffic jam is a parking lot that forgot it was supposed to stay still.\n"
    "It maps cars packed bumper to bumper and barely moving, but it leaves out "
    "that a real parking lot never moves at all, while a jam still inches forward.\n"
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 400
# characters, not only white space. Refuse to write an entry that
# would fail it, instead of silently shipping an invalid one.
assert 1 <= len(ENTRY) <= 400, "entry outside the 1-400 character gate"
assert ENTRY.strip(), "entry is only white space"
assert ENTRY.count("\n") == 2, "entry must be exactly two lines"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
