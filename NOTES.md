# Design notes — the payments database apologizes

- Framing: the apology comes from the database itself, addressed to all-staff.
- The blame lands on a script named final_v2_DEFINITELY_safe.py — the classic
  unreviewed "definitely safe" migration everyone recognizes.
- The punchline is SQL-shaped: the database refuses writes until someone says
  BEGIN out loud, turning a transaction keyword into a trust ritual.
- Kept concrete (orders table, 14:03-style workplace reality) so it reads like
  a real incident email, not a generic outage joke.
- Entry text is 192 characters, inside the 200 limit.
- main.py stays a plain writer: entry text to $OUTPUT_DIR/entry.txt (default
  /output) so reproduce works unchanged.
