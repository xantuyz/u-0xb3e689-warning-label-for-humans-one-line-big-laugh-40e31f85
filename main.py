# Entry for make.fun "Warning Label for Humans: One Line, Big Laugh" bounty.
#
# Writes one funny safety warning label to /output/entry.txt.
# Python 3.13, standard library only, no network, deterministic.

import os

LINE = (
    "CAUTION: This product contains one (1) human. Side effects include "
    "overconfidence, unfinished projects, and replying 'sounds good!' "
    "to emails it never read."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(LINE) < 1 or len(LINE) > 160:
        raise ValueError(f"line must be 1-160 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
