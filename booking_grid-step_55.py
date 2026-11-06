# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: BookingGrid
def _find_duplicate_booking(booking, existing_bookings):
    for existing in existing_bookings:
        if (
            existing.client_id == booking.client_id
            and existing.service_id == booking.service_id
            and existing.start_time == booking.start_time
            and existing.end_time == booking.end_time
            and existing.status == booking.status
        ):
            return existing
    return None

def check_duplicate_booking(booking, existing_bookings):
    """Soft duplicate check: returns a conflict message or None."""
    conflict = _find_duplicate_booking(booking, existing_bookings)
    if conflict:
        return (
            f"Дубликат: у клиента {conflict.client_name} уже есть запись на "
            f"{conflict.service_name} в интервале {conflict.start_time}–{conflict.end_time}"
        )
    return None
