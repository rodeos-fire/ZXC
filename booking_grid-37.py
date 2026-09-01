# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: BookingGrid
import unittest

class TestBookingGrid(unittest.TestCase):
    def test_slot_capacity(self):
        slot = Slot(capacity=2)
        self.assertEqual(slot.remaining_capacity(), 2)
        slot.add_client("Alice")
        self.assertEqual(slot.remaining_capacity(), 1)
        slot.add_client("Bob")
        self.assertEqual(slot.remaining_capacity(), 0)
        with self.assertRaises(OverbookingException):
            slot.add_client("Charlie")

    def test_client_booking(self):
        client = Client("Alice")
        service = Service("Haircut", price=20)
        booking = Booking(client, service, 2024, 3, 15, 10)
        self.assertEqual(booking.total_cost(), 20)

    def test_payment_refund(self):
        payment = Payment(amount=100, method="card")
        payment.process()
        self.assertEqual(payment.status, "completed")
        payment.refund()
        self.assertEqual(payment.status, "refunded")

    def test_booking_grid_layout(self):
        grid = BookingGrid()
        grid.add_slot(Slot(capacity=1, x=0, y=0))
        grid.add_slot(Slot(capacity=1, x=1, y=0))
        self.assertEqual(len(grid.slots), 2)

    def test_service_price_update(self):
        service = Service("Massage", price=50)
        service.update_price(60)
        self.assertEqual(service.price, 60)

if __name__ == "__main__":
    unittest.main()
