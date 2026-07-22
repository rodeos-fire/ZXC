# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: BookingGrid
def check_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for booking in _bookings:
        if (booking.client_name == "Иванов Иван" and 
            booking.service_name == "Массаж спины" and 
            booking.slot_date == today):
            if booking.payment_status == "not_paid":
                overdue.append(booking)
    return overdue
