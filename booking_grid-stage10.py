# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: BookingGrid
def export_to_json():
    import json
    state = {
        "slots": slots,
        "clients": clients,
        "services": services,
        "payments": payments,
        "bookings": bookings
    }
    return json.dumps(state, indent=2)
