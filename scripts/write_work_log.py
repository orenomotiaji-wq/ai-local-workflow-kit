from pathlib import Path
from datetime import datetime
import sys

def write_log(message: str):
    root = Path(__file__).resolve().parents[1]
    log_dir = root / "logs"
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "work_log.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"## {timestamp}\\n\\n{message}\\n\\n")

    print(f"Log saved: {log_file}")

if __name__ == "__main__":
    message = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "No message provided."
    write_log(message)
