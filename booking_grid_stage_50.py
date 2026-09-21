# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: BookingGrid
def _format_booking_confirmation(booking: Booking) -> str:
    """Возвращает отформатированную строку подтверждения бронирования."""
    lines = [
        "=" * 40,
        f"БРОНИРОВАНИЕ УСПЕШНО",
        "=" * 40,
        f"ID бронирования: {booking.id}",
        f"Клиент: {booking.client.name}",
        f"Услуга: {booking.service.name}",
        f"Дата: {booking.date.strftime('%d.%m.%Y')}",
        f"Время: {booking.slot}",
        f"Сумма: {booking.total_amount:.2f} {booking.currency}",
        "=" * 40,
    ]
    return "\n".join(lines)

def _format_booking_rejected(booking: Booking, reason: str = "Недостаточно средств") -> str:
    """Возвращает строку отказа бронирования с причиной."""
    lines = [
        "=" * 40,
        "БРОНИРОВАНИЕ ОТКАЗАНО",
        "=" * 40,
        f"ID бронирования: {booking.id}",
        f"Клиент: {booking.client.name}",
        f"Причина: {reason}",
        "=" * 40,
    ]
    return "\n".join(lines)

def _format_client_summary(client: Client) -> str:
    """Возвращает краткую сводку по клиенту."""
    lines = [
        "=" * 40,
        f"КЛИЕНТ: {client.name}",
        "=" * 40,
        f"ID: {client.id}",
        f"Дата рождения: {client.birth_date.strftime('%d.%m.%Y')}",
        f"Телефон: {client.phone}",
        f"Пол: {'М' if client.gender == 'M' else 'Ж'}",
        f"Статус: {'Активен' if client.is_active else 'Деактивирован'}",
        f"Бронирований: {len(client.bookings)}",
        "=" * 40,
    ]
    return "\n".join(lines)

def _format_service_catalog(service: Service) -> str:
    """Возвращает описание услуги в каталоге."""
    lines = [
        "=" * 40,
        f"УСЛУГА: {service.name}",
        "=" * 40,
        f"ID: {service.id}",
        f"Описание: {service.description}",
        f"Цена: {service.base_price:.2f} {service.currency}",
        f"Доступна: {'Да' if service.is_available else 'Нет'}",
        "=" * 40,
    ]
    return "\n".join(lines)

def _print_grid_header() -> None:
    """Выводит заголовок сетки бронирований."""
    print("=" * 60)
    print("  ПЛАНИРОВЩИК БРОНИРОВАНИЙ BOOKINGGRID")
    print("=" * 60)

def _print_grid_footer() -> None:
    """Выводит финальную строку с количеством слотов."""
    print(f"  Всего слотов в таблице: {BOOKING_GRID_ROWS * BOOKING_GRID_COLS}")
    print("=" * 60)
