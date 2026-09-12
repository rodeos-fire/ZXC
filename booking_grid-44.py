# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: BookingGrid
import shutil
from datetime import datetime

BACKUP_DIR = 'backups'

def backup_data(data_file: str, max_backups: int = 5) -> str:
    """Создаёт резервную копию файла данных с автоматическим удалением старых."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(BACKUP_DIR, f"{os.path.basename(data_file)}.backup_{timestamp}")
    shutil.copy2(data_file, backup_path)
    backup_files = sorted(os.listdir(BACKUP_DIR), reverse=True)
    if len(backup_files) > max_backups:
        for old_file in backup_files[max_backups:]:
            os.remove(os.path.join(BACKUP_DIR, old_file))
    return backup_path
