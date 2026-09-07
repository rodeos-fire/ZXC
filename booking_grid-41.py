# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: BookingGrid
def dry_run_mode():
    """Включает режим сухого прогона: операции записываются в лог, но не применяются."""
    global _dry_run
    _dry_run = True
    print("Dry-run mode enabled. No changes will be persisted.")
    return _dry_run

def disable_dry_run():
    """Выключает режим сухого прогона."""
    global _dry_run
    _dry_run = False
    print("Dry-run mode disabled.")
    return _dry_run

def log_action(action, data):
    """Записывает действие в лог вместо его выполнения."""
    if _dry_run:
        print(f"[DRY-RUN] {action}: {data}")
        return False
    else:
        print(f"[EXEC] {action}: {data}")
        return True
