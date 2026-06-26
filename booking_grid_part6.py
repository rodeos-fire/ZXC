# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: BookingGrid
def filter_bookings(status=None, category=None, tags=None):
    filtered = []
    for b in bookings:
        if status and b.status != status: continue
        if category and (b.category != category or not any(t.startswith(category) for t in b.tags)): continue
        if tags and not all(any(tag == t for t in b.tags) for tag in tags): continue
        filtered.append(b)
    return filtered

def get_bookings_by_date_range(start, end):
    start_dt = datetime.fromisoformat(start.replace('Z', '+00:00'))
    end_dt = datetime.fromisoformat(end.replace('Z', '+00:00'))
    return [b for b in bookings if start_dt <= b.created_at <= end_dt]

def get_bookings_by_user(user_id):
    return [b for b in bookings if b.user_id == user_id]
