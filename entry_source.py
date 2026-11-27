#!/usr/bin/env python3
"""Writes the bounty entry text to /output/entry.txt."""
import os

ENTRY = "I dropped production. Restore ran, backups held, every row came back — the standup now opens with my apology in three languages plus a puppet show about transaction isolation."


def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
