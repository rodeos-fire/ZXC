# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: BookingGrid
def _build_slots_for_day(day, services):
    """Build a list of (start, end, name) tuples for a given day and its services."""
    slots = []
    for svc in services:
        for h in range(svc.start_hour, svc.end_hour + 1):
            for m in range(svc.start_minute, svc.end_minute + 1, 30):
                name = f"{svc.name} {h:02d}:{m:02d}"
                slots.append((day, h, m, svc.id, name))
    return slots
