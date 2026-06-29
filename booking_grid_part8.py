# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: BookingGrid
def main_menu():
    while True:
        print("\n=== BookingGrid Menu ===")
        print("1. Показать все слоты")
        print("2. Добавить клиента")
        print("3. Занять слот клиентом")
        print("4. Вывести отчёт по услугам")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            for slot in slots:
                status = "Занято" if slot["occupied"] else "Свободно"
                print(f"{slot['id']}: {status} ({slot['service_name']})")
            
        elif choice == "2":
            name = input("Имя клиента: ")
            client_id = len(clients) + 1
            clients.append({"id": client_id, "name": name})
            print(f"Клиент {client_id} добавлен.")
            
        elif choice == "3":
            if not slots or all(s["occupied"] for s in slots):
                print("Нет свободных слотов!")
                continue
            slot_idx = int(input("Номер свободного слота: ")) - 1
            client_idx = int(input("ID клиента: ")) - 1
            if 0 <= slot_idx < len(slots) and 0 <= client_idx < len(clients):
                slots[slot_idx]["occupied"] = True
                slots[slot_idx]["client_id"] = clients[client_idx]["id"]
                print(f"Слот {slots[slot_idx]['id']} забронирован клиентом {clients[client_idx]['name']}.")
            else:
                print("Неверные индексы слота или клиента.")
                
        elif choice == "4":
            for service in services:
                count = sum(1 for s in slots if not s["occupied"] and s.get("service_id") == service["id"])
                print(f"{service['name']}: {count} свободных слотов")
            
        elif choice == "5":
            with open("booking_grid.json", "w", encoding="utf-8") as f:
                json.dump({"slots": slots, "clients": clients, "services": services}, f, ensure_ascii=False)
            print("Данные сохранены. До свидания!")
            break
            
        else:
            print("Неверный выбор.")
