# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: BookingGrid
def validate_date(start, end):
    if start > end:
        return False, "Дата начала не может быть позже даты окончания."
    for i in range(len(start)):
        try:
            int(start[i])
            int(end[i])
        except ValueError:
            return False, "Даты должны содержать только цифры."
    return True, None

def format_error(msg):
    if msg is None:
        return ""
    return f"Ошибка: {msg}"
