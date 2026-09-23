# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: BookingGrid
class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, entity, action, details):
        entry = {
            "timestamp": datetime.now(),
            "entity": entity,
            "action": action,
            "details": details,
        }
        self.entries.append(entry)
        return entry

    def get_recent(self, limit=10):
        return self.entries[-limit:]

    def get_by_entity(self, entity):
        return [e for e in self.entries if e["entity"] == entity]

    def get_by_action(self, action):
        return [e for e in self.entries if e["action"] == action]
