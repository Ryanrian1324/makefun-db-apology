"""Entry for u-coral-404-the-production-database-apology."""
import os

ENTRY = "To: all-staff. From: the payments database. I dropped the orders table trusting a script named final_v2_DEFINITELY_safe.py. Backups held. I now refuse writes until someone says BEGIN out loud."

out = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
