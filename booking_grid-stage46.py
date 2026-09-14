# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: BookingGrid
def migrate_to_v2():
    """Migration to version 2: add payment status tracking to bookings."""
    # In a real database context, this would generate SQL ALTER statements.
    # For this in-memory project, we update the schema definition directly.
    global BOOKING_SCHEMA
    BOOKING_SCHEMA = (
        "BookingID", "ClientID", "ServiceID", "SlotID", "PaymentMethod",
        "PaymentStatus", "CreatedAt", "UpdatedAt"
    )
    print("Migration v1->v2 complete: PaymentStatus field added to Booking model.")
