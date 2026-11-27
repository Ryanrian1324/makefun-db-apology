#!/usr/bin/env python3
"""Writes the db-apology entry text to $OUTPUT_DIR/entry.txt (default /output)."""
import os

ENTRY = 'I dropped the production database. Backups held, data restored in 40 minutes, and the only casualty is my name in the standup notes — where it is now a unit of time: "one Ryan" = one self-inflicted outage.'

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
