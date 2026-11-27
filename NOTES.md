# Design notes — Dropped Prod, Kept the Backups

- Story: an accidental production database drop, saved by backups.
- The joke lands on the aftermath: "one Ryan" becomes a unit of time for a self-inflicted outage.
- Details kept concrete (40 minutes, standup notes) so the apology reads real, not generic.
- main.py stays a plain writer: entry text to $OUTPUT_DIR/entry.txt (default /output) so reproduce works unchanged.
