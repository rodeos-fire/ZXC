# === Stage 17: Добавь группировку записей по категориям ===
# Project: BookingGrid
def group_bookings_by_category(booking_list):
    """Group booking records by service category."""
    categories = {}
    for record in booking_list:
        cat = record.get('category', 'Uncategorized')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(record)
    return categories

def print_grouped_bookings(grouped):
    """Pretty-print grouped bookings."""
    for category, records in sorted(grouped.items()):
        print(f"[{category}]")
        for r in records:
            name = r.get('client_name', 'Unknown')
            date = r.get('date', '?')
            amount = r.get('amount', 0)
            status = r.get('status', 'Pending')
            print(f"  - {name} | {date} | ${amount:.2f} [{status}]")

# Example usage:
sample_bookings = [
    {"client_name": "Alice", "category": "Haircut", "date": "2025-12-01", "amount": 35.0, "status": "Confirmed"},
    {"client_name": "Bob",   "category": "Shave",    "date": "2025-12-02", "amount": 15.0, "status": "Pending"},
    {"client_name": "Alice", "category": "Haircut", "date": "2025-12-03", "amount": 40.0, "status": "Confirmed"},
    {"client_name": "Carol", "category": "Massage", "date": "2025-12-01", "amount": 60.0, "status": "Pending"},
]

grouped = group_bookings_by_category(sample_bookings)
print_grouped_bookings(grouped)
