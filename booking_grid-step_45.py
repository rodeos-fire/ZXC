# === Stage 45: Добавь восстановление из резервной копии ===
# Project: BookingGrid
import json, os

def load_from_backup(backup_path):
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Резервная копия не найдена: {backup_path}")
    with open(backup_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def save_to_backup(data, backup_path):
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    backup_file = "booking_backup.json"
    data = load_from_backup(backup_file)
    save_to_backup(data, backup_file)
    print(f"Резервная копия сохранена: {backup_file}")
