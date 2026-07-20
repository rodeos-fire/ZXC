# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: BookingGrid
class Reminder:
    def __init__(self, booking_id, date, message):
        self.booking_id = booking_id
        self.date = date
        self.message = message

    def remind(self):
        if datetime.now() >= self.date:
            print(f"Напоминание! Запись {self.booking_id}: {self.message}")
            return True
        return False
