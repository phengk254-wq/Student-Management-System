import os
import shutil
from datetime import datetime

UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(UTILS_DIR)
DB_DIR = os.path.join(ROOT_DIR, "database")
BACKUP_DIR = os.path.join(DB_DIR, "backup")

ADMIN_FILE = os.path.join(DB_DIR, "admins.txt")
TEACHER_FILE = os.path.join(DB_DIR, "teachers.txt")
STUDENT_FILE = os.path.join(DB_DIR, "students.txt")

DELIMITER = " | "

def ensure_db_ready():
    
    os.makedirs(DB_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for f in (ADMIN_FILE, TEACHER_FILE, STUDENT_FILE):
        if not os.path.exists(f):
            open(f, "w", encoding="utf-8").close()

def read_lines(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip()]
    
def write_lines(filepath, lines):
    with open(filepath, "w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line + "\n")

def append_line(filepath, line):
    with open(filepath, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")

def load_records(filepath):
    return [line.split(DELIMITER) for line in read_lines(filepath)]

def save_records(filepath, records):
    lines = [DELIMITER.join(record) for record in records]
    write_lines(filepath, lines)

def generate_id(prefix, filepath):
    records = load_records(filepath)
    max_num = 0
    for rec in records:
        if rec[0].startswith(prefix):
            try:
                num = int(rec[0][len(prefix):])
                max_num = max(max_num, num)
            except ValueError:
                continue
    return f"{prefix}{max_num + 1:03d}"

def backup_database():
    ensure_db_ready()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target_dir = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(target_dir, exist_ok=True)
    for f in (ADMIN_FILE, TEACHER_FILE, STUDENT_FILE):
        if os.path.exists(f):
            shutil.copy(f, target_dir)
    return target_dir

def list_backups():
    ensure_db_ready()
    if not os.path.exists(BACKUP_DIR):
        return []
    return sorted(
        [d for d in os.listdir(BACKUP_DIR) if os.path.isdir(os.path.join(BACKUP_DIR, d))],
        reverse=True,
    )

def restore_database(backup_name):
    source_dir = os.path.join(BACKUP_DIR, backup_name)
    if not os.path.isdir(source_dir):
        return False
    for filename in ("admins.txt", "teachers.txt", "students.txt"):
        src = os.path.join(source_dir, filename)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(DB_DIR, filename))
    return True