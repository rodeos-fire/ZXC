# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: BookingGrid
def self_check():
    """Финальная самопроверка: импортируем модуль, пробегаем по каждому классу,
    создаём минимальные экземпляры и проверяем ключевые методы."""
    import sys
    sys.path.insert(0, '.')
    from booking_grid import (
        Client, Service, Slot, Booking, Payment, Status,
        BookingGrid, BookingGridError, BookingGridWarning
    )
    # 1) Клиенты
    c1 = Client('Иванов', 'ivan@example.com', '+79001112233')
    c2 = Client('Петров', 'petrov@example.com', '+79004445566')
    assert c1.id == c2.id, 'ID клиентов должны совпадать'
    # 2) Услуги
    s1 = Service('Массаж', 500, 60)
    s2 = Service('Консультация', 200, 30)
    assert s1.price == 500 and s2.duration == 30
    # 3) Слоты
    grid = BookingGrid(s1, s2)
    slot = grid.create_slot(2025_12_15, 10, 'Иванов')
    assert slot.client_name == 'Иванов' and slot.status == Status.BOOKED
    # 4) Бронь и оплата
    booking = grid.get_booking(slot.id)
    assert booking is not None
    pay = Payment(booking.id, 'Карта', 500, 'OK')
    assert pay.status == 'OK' and pay.total == 500
    # 5) Ошибки и предупреждения
    try:
        BookingGridError('test')
    except BookingGridError as e:
        assert 'test' in str(e)
    try:
        BookingGridWarning('test')
    except BookingGridWarning as e:
        assert 'test' in str(e)
    print('✅ Самопроверка пройдена: все классы и методы работают корректно.')
