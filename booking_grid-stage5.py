# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: BookingGrid
def delete_record(entity_type, record_id):
    if entity_type not in data:
        print(f"Ошибка: тип записи '{entity_type}' не найден.")
        return False
    records = data[entity_type]
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} для типа '{entity_type}' не найдена.")
        return False
    del records[record_id]
    print(f"Запись успешно удалена.")
    return True

def handle_missing_ids(entity_type, record_id):
    if entity_type not in data:
        raise ValueError(f"Неизвестный тип сущности: {entity_type}")
    if record_id is None or (isinstance(record_id, str) and not record_id.strip()):
        print("ID записи не может быть пустым.")
        return False
    records = data[entity_type]
    if record_id in records:
        del records[record_id]
        return True
    else:
        print(f"Запись с ID {record_id} отсутствует в базе данных.")
        return False

# Пример использования (раскомментируйте для тестирования)
# delete_record('services', 999)
# handle_missing_ids('clients', None)
