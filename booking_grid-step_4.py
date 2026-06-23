# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: BookingGrid
def edit_booking(booking_id, updates):
    bookings = get_bookings()
    if not bookings: return False
    for i, b in enumerate(bookings):
        if b['id'] == booking_id:
            bookings[i].update(updates)
            save_bookings(bookings)
            print(f"Booking {booking_id} updated.")
            return True
    print("Booking not found.")
    return False
