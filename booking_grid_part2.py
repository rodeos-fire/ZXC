# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: BookingGrid
class BookingModel:
    def __init__(self, client_name: str, service_id: int, slot_date: str, slot_time: str):
        self.client_name = client_name.strip()
        self.service_id = service_id
        self.slot_date = slot_date
        self.slot_time = slot_time

    @property
    def is_valid(self) -> bool:
        return (self.client_name and len(self.client_name) <= 50 and
                isinstance(self.service_id, int) and 1 <= self.service_id <= 9999 and
                len(self.slot_date) == 8 and self.slot_date.isdigit() and
                len(self.slot_time) == 5 and self.slot_time[2] == ':' and self.slot_time[:2].isdigit() and self.slot_time[3:5].isdigit())

    def get_formatted_slot(self) -> str:
        return f"{self.slot_date} {self.slot_time}"
