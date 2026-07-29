# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: BookingGrid
def reset_demo_data():
    """Сбрасывает демо-данные: удаляет всех клиентов, услуг, бронирований и оплат."""
    global clients, services, bookings, payments, slots
    # Очищаем списки данных
    clients = []
    services = []
    bookings = []
    payments = []
    # Перезапускаем слоты с базовыми параметрами
    slots = {
        "date": datetime.date.today(),
        "slots_per_day": 24,
        "slot_duration_minutes": 60,
        "start_hour": 9,
        "end_hour": 18,
        "available_slots": [],
        "booked_slots": []
    }
    _generate_available_slots()


def clear_state():
    """Полностью очищает все данные и сбрасывает в начальное состояние."""
    reset_demo_data()
