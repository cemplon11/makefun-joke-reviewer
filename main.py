#!/usr/bin/env python3
"""make.fun entry: writes one one-line joke about working beside AI coding
agents to /output/entry.txt. Pure Python 3.13 standard library, no network,
deterministic: every run writes the same bytes."""

import os

JOKE = (
    "The agent's commit message said 'fixed everything' \u2014 the diff "
    "touched 47 files, and the bug is still there, now with friends."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
