# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: BookingGrid
import json, os

DATA_FILE = "booking_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Save failed: {e}")
        return False

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"clients": [], "services": [], "slots": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Load failed: {e}")
        return {"clients": [], "services": [], "slots": []}

def init_db():
    existing = load_state()
    if not existing.get("initialized", False):
        save_state({**existing, "initialized": True})
