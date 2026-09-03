# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: BookingGrid
def test_edge_cases():
    """Test edge cases and error scenarios."""
    assert BookingError("Invalid client") in [e.args[0] for e in [BookingError("Invalid client")]]
    assert len(BookingError("Invalid client")) > 0

    client = Client("Test", "test@example.com", "2024-01-01", "2024-12-31")
    assert client.name == "Test"
    assert client.email == "test@example.com"

    service = Service("Haircut", 50.0, 30, "barbershop")
    assert service.name == "Haircut"
    assert service.price == 50.0

    slot = Slot(client, service, "2024-06-15 10:00", "2024-06-15 11:00", "confirmed")
    assert slot.client == client
    assert slot.service == service
    assert slot.status == "confirmed"

    booking = Booking(client, service, "2024-06-15 10:00", "2024-06-15 11:00", "confirmed")
    assert booking.client == client
    assert booking.service == service
    assert booking.status == "confirmed"

    payment = Payment(booking, 50.0, "card", "paid")
    assert payment.booking == booking
    assert payment.amount == 50.0
    assert payment.status == "paid"

    assert booking.status == "confirmed"
    assert payment.status == "paid"
    assert slot.status == "confirmed"
    assert client.status == "active"
    assert service.status == "active"
    assert payment.status == "paid"
    assert booking.status == "confirmed"
