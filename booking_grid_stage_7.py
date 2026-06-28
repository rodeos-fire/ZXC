# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: BookingGrid
def sort_bookings(bookings, key='date'):
    if not bookings: return []
    reverse = False
    if key == 'priority': reverse = True
    elif key == 'name': pass
    else: key = 'date'
    def get_sort_val(b):
        try: return b['date'] or 0
        except: return 0
    def get_priority(b):
        try: return -b.get('priority', 1) if reverse else b.get('priority', 1)
        except: return 0
    def get_name(b):
        try: return b['name'] or ''
        except: return ''
    sort_key = { 'date': (get_sort_val, False), 'priority': (get_priority, True), 'name': (get_name, False) }[key]
    key_func, rev = sort_key[key], sort_key.get(key, ('', False))
    try: val_fn, is_rev = key_func, reverse if key == 'priority' else False
    except: val_fn, is_rev = get_sort_val, False
    return sorted(bookings, key=lambda x: (val_fn(x), -x['id']), reverse=is_rev)
