# === Stage 20: Добавь восстановление записей из архива ===
# Project: BookingGrid
def restore_from_archive(archive_path, output_path):
    """Восстановляет записи из текстового архива в формат JSON."""
    with open(archive_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    records = []
    for line in lines:
        try:
            record = json.loads(line)
            records.append(record)
        except json.JSONDecodeError:
            continue
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
