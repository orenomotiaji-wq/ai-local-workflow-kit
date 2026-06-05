from pathlib import Path
from datetime import datetime
import shutil
import sys

def create_backup(target_path: str):
    target = Path(target_path).expanduser().resolve()

    if not target.exists():
        print(f"ERROR: File not found: {target}")
        return

    root = Path(__file__).resolve().parents[1]
    backup_dir = root / "backups"
    backup_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{target.name}.{timestamp}.bak"
    backup_path = backup_dir / backup_name

    shutil.copy2(target, backup_path)
    print(f"Backup created: {backup_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/create_backup.py <file_path>")
    else:
        create_backup(sys.argv[1])
