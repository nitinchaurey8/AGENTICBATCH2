import re
from pathlib import Path

root = Path(r"g:/agenticbatch2")
patterns = [
    (re.compile(r"lsv2_pt_[A-Za-z0-9_]+"), "lsv2_pt_REDACTED"),
    (re.compile(r"gsk_[A-Za-z0-9]+"), "gsk_REDACTED"),
    (re.compile(r"sk-proj-[A-Za-z0-9_-]+"), "sk-proj-REDACTED"),
    (re.compile(r"hf_[A-Za-z0-9]+"), "hf_REDACTED"),
]

changed = 0
for path in root.rglob("*.ipynb"):
    if "venv" in path.parts:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    original = text
    for rx, repl in patterns:
        text = rx.sub(repl, text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed += 1

print(f"Sanitized notebooks: {changed}")
