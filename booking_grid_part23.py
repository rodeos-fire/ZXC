# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: BookingGrid
def print_booking_table(grid):
    """Выводит таблицу бронирований в консоль."""
    if not grid:
        print("Нет данных для отображения.")
        return
    for slot in grid:
        print(f"Слот {slot['id']}: "
              f"Клиент={slot.get('client', {}).get('name', 'N/A')}, "
              f"Услуга={slot.get('service', {}).get('name', 'N/A')}, "
              f"Статус={slot.get('status', 'unknown')}")
