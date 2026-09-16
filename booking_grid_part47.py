# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: BookingGrid
def demo():
    """Демонстрация пользовательского сценария: клиент бронирует услугу."""
    from datetime import datetime, timedelta
    now = datetime.now()

    # Создаём клиента
    client = Client(name="Алексей Петров", email="alex@example.com", phone="+79990000001")

    # Создаём услугу
    service = Service(name="Массаж спины", duration_minutes=60, price=3000, category="SPA")

    # Создаём слоты
    slot1 = Slot(date=now, hour=10, minute=0, service=service, client=client)
    slot2 = Slot(date=now, hour=14, minute=0, service=service, client=client)
    slot3 = Slot(date=now, hour=20, minute=0, service=service, client=client)

    # Бронируем слоты
    booking1 = Booking(slot=slot1, status="confirmed")
    booking2 = Booking(slot=slot2, status="pending")
    booking3 = Booking(slot=slot3, status="cancelled")

    # Оплаты
    payment1 = Payment(amount=3000, currency="RUB", method="card", booking=booking1)
    payment2 = Payment(amount=3000, currency="RUB", method="card", booking=booking2)

    # Выводим результаты
    print(f"Клиент: {client.name}")
    print(f"Услуга: {service.name} ({service.duration_minutes} мин, {service.price} руб)")
    print(f"Слот 1 (10:00) - Бронь: {booking1.status}, Оплата: {payment1.method}")
    print(f"Слот 2 (14:00) - Бронь: {booking2.status}, Оплата: {payment2.method}")
    print(f"Слот 3 (20:00) - Бронь: {booking3.status} (отменена)")
    print(f"Всего подтверждённых броней: {len([b for b in [booking1, booking2, booking3] if b.status == 'confirmed'])}")
