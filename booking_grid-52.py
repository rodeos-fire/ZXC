# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: BookingGrid
def export_report(bookings, services, clients):
    lines = []
    lines.append("=== BookingGrid Report ===")
    lines.append(f"Total bookings: {len(bookings)}")
    lines.append("")
    for b in bookings:
        lines.append(f"Client: {b['client']}")
        lines.append(f"Service: {b['service']}")
        lines.append(f"Date: {b['date']}")
        lines.append(f"Price: {b['price']}")
        lines.append(f"Status: {b['status']}")
        lines.append("")
    lines.append("=== End Report ===")
    return "\n".join(lines)
