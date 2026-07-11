# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: BookingGrid
def weekly_stats(booking_grid):
    stats = {}
    for booking in booking_grid:
        start = booking['start']
        end = booking['end']
        weekday = start.weekday()
        slot_type = booking.get('slot_type', 'unknown')
        key = (weekday, slot_type)
        if key not in stats:
            stats[key] = []
        stats[key].append(booking)
    return {f"{w} - {t}": bookings for (w, t), bookings in stats.items()}
