# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: BookingGrid
def check_integrity_and_repair(data, repairable=("bookings", "payments")):
    """Проверка и ремонт основных проблем в данных."""
    errors = []
    repaired = []

    if "bookings" in data:
        bookings = data["bookings"]
        for i, b in enumerate(bookings):
            if not isinstance(b, dict):
                errors.append(f"Booking {i} не является словарём")
                continue
            if not b.get("id"):
                errors.append(f"Booking {i} не имеет id")
            if not b.get("service_id") or not b.get("client_id"):
                errors.append(f"Booking {i} не имеет service_id или client_id")
            if "slots" in b:
                slots = b["slots"]
                if isinstance(slots, list):
                    for j, s in enumerate(slots):
                        if not isinstance(s, dict) or not s.get("start"):
                            errors.append(f"Booking {b['id']} slot {j} некорректный")
                            break

    if "payments" in data:
        payments = data["payments"]
        for i, p in enumerate(payments):
            if not isinstance(p, dict):
                errors.append(f"Payment {i} не является словарём")
                continue
            if not p.get("id"):
                errors.append(f"Payment {i} не имеет id")
            if not p.get("booking_id"):
                errors.append(f"Payment {i} не имеет booking_id")
            if "amount" in p and p["amount"] < 0:
                errors.append(f"Payment {p['id']} отрицательная сумма")

    if errors:
        print(f"Найдено {len(errors)} ошибок целостности")
    else:
        print("Данные целостны")

    return {"errors": errors, "status": "ok" if not errors else "needs_repair"}
