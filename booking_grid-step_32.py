# === Stage 32: Добавь журнал действий пользователя ===
# Project: BookingGrid
class ActionLog:
    def __init__(self):
        self._log = []

    def log(self, action: str, detail: str):
        entry = {"timestamp": datetime.now().isoformat(), "action": action, "detail": detail}
        self._log.append(entry)
        print(f"[{entry['timestamp']}] {action}: {detail}")

    def get_log(self) -> list:
        return list(self._log)
