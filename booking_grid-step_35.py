# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: BookingGrid
def next_action(state):
    """Recommends the next action based on the current state."""
    if state.get("has_client", False) and not state.get("has_service", False):
        return "Select a service"
    if state.get("has_service", False) and not state.get("has_slot", False):
        return "Select a time slot"
    if state.get("has_slot", False) and not state.get("has_payment", False):
        return "Confirm payment"
    return "Booking complete"
