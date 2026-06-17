# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: BookingGrid
import json, uuid
from datetime import datetime, timedelta
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional

@dataclass
class Client:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    email: str = ""

@dataclass
class Service:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    duration_minutes: int = 60

@dataclass
class TimeSlot:
    start_time: datetime
    end_time: datetime
    booked_client_id: Optional[str] = None

def initialize_booking_grid():
    clients_db: Dict[str, Client] = {
        "c1": Client(name="Иван Иванов", email="ivan@example.com"),
        "c2": Client(name="Мария Петрова", email="maria@example.com")
    }
    
    services_db: Dict[str, Service] = {
        "s1": Service(name="Консультация", duration_minutes=30),
        "s2": Service(name="Аудит", duration_minutes=90)
    }
    
    slots_db: List[TimeSlot] = []
    for day_offset in range(7):
        current_date = datetime.now().date() + timedelta(days=day_offset)
        base_time = datetime.combine(current_date, datetime.min.time())
        hour = 10
        while hour < 20:
            slot_start = base_time.replace(hour=hour, minute=0)
            slot_end = base_time.replace(hour=hour+1, minute=0)
            slots_db.append(TimeSlot(start_time=slot_start, end_time=slot_end))
            hour += 1
            
    return clients_db, services_db, slots_db

if __name__ == "__main__":
    print("Инициализация BookingGrid...")
    clients, services, slots = initialize_booking_grid()
    print(f"Загружено клиентов: {len(clients)}")
    print(f"Загружено услуг: {len(services)}")
    print(f"Создано слотов времени: {len(slots)}")
