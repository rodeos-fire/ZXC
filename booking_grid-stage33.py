# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: BookingGrid
class UndoManager:
    def __init__(self, max_steps=10):
        self._history = []
        self._max_steps = max_steps

    def _snapshot(self):
        state = {
            'slots': list(BookingGrid.slots),
            'clients': list(BookingGrid.clients),
            'services': list(BookingGrid.services),
            'payments': list(BookingGrid.payments),
        }
        self._history.append(state)
        if len(self._history) > self._max_steps:
            self._history.pop(0)

    def undo(self):
        if not self._history:
            return False
        prev = self._history.pop()
        for key in prev:
            key_map = {
                'slots': BookingGrid.slots,
                'clients': BookingGrid.clients,
                'services': BookingGrid.services,
                'payments': BookingGrid.payments,
            }
            key_map[key].clear()
            key_map[key].extend(prev[key])
        return True

    def redo(self):
        if not self._history:
            return False
        state = self._history.pop()
        for key in state:
            key_map = {
                'slots': BookingGrid.slots,
                'clients': BookingGrid.clients,
                'services': BookingGrid.services,
                'payments': BookingGrid.payments,
            }
            key_map[key].extend(state[key])
        return True
