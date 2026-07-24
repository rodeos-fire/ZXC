# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: BookingGrid
def print_booking_record(b: Booking) -> None:
    if b is None:
        return
    from datetime import date, timedelta
    start = b.start_date or date.today() - timedelta(days=30)
    end = b.end_date or (start + timedelta(days=b.duration))
    total = sum((b.price_per_slot * i for i in range(b.duration if b.duration else 1)))
    print(f"Booking: {b.id} | Client: {b.client_name} | Service: {b.service_name}")
    print(f"  Dates: {start.date()} – {end.date()} ({b.duration} slots) | Price/slot: {b.price_per_slot}")
    print(f"  Total cost: {total} | Status: {b.status}")
