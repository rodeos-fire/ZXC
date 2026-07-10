# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: BookingGrid
def generate_summary():
    """Генерация краткой сводки по текущим данным."""
    total_slots = len(slots) if slots else 0
    total_clients = len(clients) if clients else 0
    total_services = len(services) if services else 0
    total_payments = sum(len(payments.get(id, [])) for id in payments.keys()) if payments else 0
    
    summary = (
        f"BookingGrid Сводка:\n"
        f"- Слоты: {total_slots}\n"
        f"- Клиенты: {total_clients}\n"
        f"- Услуги: {total_services}\n"
        f"- Оплаты: {total_payments}"
    )
    print(summary)
