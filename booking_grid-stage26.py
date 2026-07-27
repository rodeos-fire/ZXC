# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: BookingGrid
def run_demo():
    """Демо-команды для ручного тестирования BookingGrid."""
    from booking_grid import (
        BookingGrid, SlotType, Client, Service, Payment,
        BookingStatus, BookingError
    )
    
    grid = BookingGrid(
        rows=3, cols=5, slot_types=[SlotType.SINGLE, SlotType.DOUBLE],
        client_classes=[Client.BASIC, Client.PREMIUM]
    )
    
    # Заполняем слоты разными типами
    for r in range(3):
        for c in range(5):
            grid.set_slot(r, c, SlotType.SINGLE)
    
    # Создаём клиентов и бронируем несколько мест
    alice = Client.BASIC("Alice", "alice@example.com")
    bob = Client.PREMIUM("Bob", "bob@example.com")
    charlie = Client.BASIC("Charlie", "charlie@example.com")
    
    grid.book_slot(0, 0, alice, SlotType.SINGLE)
    grid.book_slot(0, 1, bob, SlotType.DOUBLE)
    grid.book_slot(1, 2, charlie, SlotType.SINGLE)
    grid.book_slot(2, 4, alice, SlotType.SINGLE)
    
    # Показываем результат
    print("=== Демо-отчёт ===")
    for r in range(grid.rows):
        line = f"Ряд {r}:"
        for c in range(grid.cols):
            slot = grid.get_slot(r, c)
            if slot:
                client_name = slot.client.name
                service = slot.service.name if slot.service else "Нет"
                status = slot.status.name
                line += f" [{client_name}|{service}|{status}]"
            else:
                line += f" [пусто]"
        print(line)
    
    # Проверяем доступные слоты
    available = grid.get_available_slots()
    print(f"\nДоступных слотов: {len(available)}")
    
    # Пытаемся забронировать занятое место (должно вызвать ошибку)
    try:
        grid.book_slot(0, 0, charlie, SlotType.SINGLE)
        print("ОШИБКА: Бронь в уже занятом слоте прошла успешно!")
    except BookingError as e:
        print(f"\n✓ Ожиданная ошибка при двойной брони: {e}")

if __name__ == "__main__":
    run_demo()
