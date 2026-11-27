#!/usr/bin/env python3
import os

TEXT = (
    "I dropped the production database. Backups held, data restored in 40 "
    "minutes, and the only casualty is my name in the standup notes, where "
    "it is now a unit of time: one Ryan equals one self-inflicted outage, "
    "unverified at press time. The backups kept the faith."
)

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
