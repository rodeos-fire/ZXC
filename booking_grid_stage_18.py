# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: BookingGrid
class Tag:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<Tag {self.name}>"


class BookingGrid:
    def __init__(self):
        self._slots = {}
        self._clients = {}
        self._services = []
        self._payments = []
        self._tags = {}
    
    def add_slot(self, date, time, service_id, client_id=None):
        key = (date, time)
        if key not in self._slots:
            self._slots[key] = {'service_id': service_id, 'client_id': client_id}
        return self._slots[key]['client_id']
    
    def get_slot_info(self, date, time):
        key = (date, time)
        if key not in self._slots:
            raise KeyError("Слот не найден")
        return {'service_id': self._slots[key]['service_id'], 'client_id': self._slots[key].get('client_id')}
    
    def add_client(self, name):
        client_id = len(self._clients) + 1
        if client_id not in self._clients:
            self._clients[client_id] = {'name': name}
        return self._clients
    
    def get_client_info(self, client_id):
        if client_id not in self._clients:
            raise KeyError("Клиент не найден")
        return self._clients[client_id]
    
    def add_service(self, name):
        service_id = len(self._services) + 1
        if service_id not in [s['id'] for s in self._services]:
            svc = {'id': service_id, 'name': name}
            self._services.append(svc)
        return self._services
    
    def get_service_info(self, service_id):
        for svc in self._services:
            if svc['id'] == service_id:
                return svc
        raise KeyError("Услуга не найдена")
    
    def add_payment(self, amount, client_id=None):
        payment = {'amount': amount, 'client_id': client_id}
        self._payments.append(payment)
        return self._payments
    
    def get_payments_by_client(self, client_id):
        return [p for p in self._payments if p['client_id'] == client_id]
    
    def add_tag(self, name):
        tag = Tag(name)
        if name not in self._tags:
            self._tags[name] = tag
        return self._tags
    
    def remove_tag(self, name):
        if name in self._tags:
            del self._tags[name]
        else:
            raise KeyError("Тег не найден")
