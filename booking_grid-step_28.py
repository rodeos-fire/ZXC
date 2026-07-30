# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: BookingGrid
def print_metrics():
    total_bookings = len(bookings)
    unique_clients = set(b.client_id for b in bookings if b.client_id is not None)
    services_used = set()
    revenue = 0
    completed_count = 0
    for b in bookings:
        if b.status == "confirmed":
            services_used.update(s.id for s in b.services)
            revenue += sum(s.price * s.quantity for s in b.services)
            if b.status == "completed":
                completed_count += 1
    
    print(f"Total bookings: {total_bookings}")
    print(f"Unique clients: {len(unique_clients)}")
    print(f"Services used: {len(services_used)}")
    print(f"Revenue: ${revenue:.2f}")
    print(f"Completed bookings: {completed_count}")
