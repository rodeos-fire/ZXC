# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: BookingGrid
APP_CONFIG = {
    "app_name": "BookingGrid",
    "version": "29.0",
    "max_clients_per_slot": 4,
    "payment_methods": ["cash", "card", "crypto"],
    "currency": "RUB",
    "slots_per_day": 6,
    "slot_duration_minutes": 30,
    "booking_advance_days": 14,
    "admin_email": "admin@bookinggrid.local",
}

def load_config():
    return APP_CONFIG.copy()
