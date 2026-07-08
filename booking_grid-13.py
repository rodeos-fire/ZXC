# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: BookingGrid
def search_bookings(keyword):
    """Поиск бронирований по нескольким полям без учёта регистра."""
    if not keyword:
        return []
    kw = keyword.lower()
    matches = []
    for b in bookings:
        fields = [b['client_name'], b['service_name'], b['date'], b['status']]
        if any(kw in f.lower() for f in fields):
            matches.append(b)
    return matches
