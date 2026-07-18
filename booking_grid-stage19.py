# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: BookingGrid
def archive_old_records(cutoff_date=None):
    if cutoff_date is None:
        cutoff_date = datetime.now() - timedelta(days=30)
    archived = []
    active_ids = set()
    for booking in bookings:
        if booking["status"] == "completed" and booking["booked_at"] < cutoff_date:
            booking["archived"] = True
            archived.append(booking)
        else:
            active_ids.add(booking["id"])
    return archived, list(active_ids)
