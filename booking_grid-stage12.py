# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: BookingGrid
def load_data_from_json(filepath):
    """Загружает данные из JSON-файла, обрабатывая ошибки."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из '{filepath}'")
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл '{filepath}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: некорректный формат JSON в файле '{filepath}'.")
        return None
    except PermissionError:
        print(f"Ошибка: нет прав доступа к файлу '{filepath}'.")
        return None
    except Exception as e:
        print(f"Непредвиденная ошибка при загрузке данных: {e}")
        return None
