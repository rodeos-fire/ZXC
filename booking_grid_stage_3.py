# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: BookingGrid
class BookingGridState:
    def __init__(self):
        self.clients = {}
        self.services = {}
        self.bookings = []
        self.payments = []

    def add_client(self, name: str, email: str) -> int:
        if not self.clients.get(name):
            client_id = len(self.clients) + 1
            self.clients[name] = {"email": email, "id": client_id}
            return client_id
        return self.clients[name]["id"]

    def add_service(self, name: str, price: float) -> int:
        if not self.services.get(name):
            service_id = len(self.services) + 1
            self.services[name] = {"price": price, "id": service_id}
            return service_id
        return self.services[name]["id"]

    def add_booking(self, client_name: str, service_name: str, date: str):
        client_id = self.clients.get(client_name)
        if not client_id or not self.services.get(service_name):
            raise ValueError("Client or Service not found")
        booking_id = len(self.bookings) + 1
        self.bookings.append({
            "id": booking_id,
            "client_id": client_id["email"],
            "service_id": service_name,
            "date": date,
            "status": "pending"
        })

    def add_payment(self, booking: dict, amount: float):
        payment_id = len(self.payments) + 1
        self.payments.append({
            "id": payment_id,
            "booking_id": booking["id"],
            "amount": amount,
            "status": "completed"
        })
