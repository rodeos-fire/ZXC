# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: BookingGrid
def monthly_stats_by_date(bookings, start, end):
    """Return dict {date_str: {'days': {...}, 'total_slots', 'booked_slots'}} per month."""
    from datetime import date, timedelta
    if not bookings or start is None or end is None:
        return {}
    result = {}
    cur = start.replace(day=1)
    while cur < end:
        nxt = (cur + timedelta(days=32)).replace(day=1)
        month_days = {}
        total_booked = 0
        for b in bookings:
            if isinstance(b, dict):
                s = date.fromisoformat(b['start'])
                e = date.fromisoformat(b['end'])
                slots = int(b.get('slots', 1))
            else:
                continue
            if not (cur <= s < nxt and cur <= e <= nxt):
                continue
            for d in range((s - cur).days, (e - cur).days + 1):
                dt = cur + timedelta(days=d)
                month_days[dt] = month_days.get(dt, {'booked': 0})['booked'] + slots
                total_booked += slots
        for d in range((nxt - cur).days):
            month_days[cur + timedelta(days=d)] = month_days.get(cur + timedelta(days=d), {'booked': 0})
        result[cur.isoformat()] = {
            'days': {dt.isoformat(): v['booked'] for dt, v in sorted(month_days.items())},
            'total_slots': total_booked
        }
        cur = nxt
    return result
