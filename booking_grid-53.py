# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: BookingGrid
def load_records(filename):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            if len(parts) != 4:
                continue
            try:
                records.append({
                    'client': parts[0].strip(),
                    'service': parts[1].strip(),
                    'date': parts[2].strip(),
                    'time': parts[3].strip(),
                    'amount': float(parts[4].strip() or 0)
                })
            except ValueError:
                continue
    return records
