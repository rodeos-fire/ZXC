# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: BookingGrid
import json, sys

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        
        required_keys = ["services", "clients", "slots"]
        missing = [k for k in required_keys if k not in data]
        if missing:
            raise KeyError(f"Missing keys: {', '.join(missing)}")
        
        # Normalize service slots to a list of dicts with 'start' and 'end' times
        services_data = {}
        for svc_id, svc_info in data.get("services", {}).items():
            if isinstance(svc_info, dict):
                slot_list = []
                raw_slots = svc_info.get("slots", [])
                if isinstance(raw_slots, list):
                    for s in raw_slots:
                        if isinstance(s, str):
                            # Parse "HH:MM-HH:MM" format
                            parts = s.split("-")
                            if len(parts) == 2:
                                slot_list.append({"start": parts[0], "end": parts[1]})
                services_data[svc_id] = {"name": svc_info.get("name", ""), "slots": slot_list}

        # Normalize clients to a list of dicts with 'id' and 'name'
        clients_data = []
        for c in data.get("clients", []):
            if isinstance(c, dict):
                clients_data.append({"id": c.get("id"), "name": c.get("name")})

        # Normalize slots to a list of dicts with 'date', 'service_id' and calculated availability
        slots_data = []
        for svc_id, svc_info in services_data.items():
            for slot in svc_info["slots"]:
                start_time = slot["start"]
                end_time = slot["end"]
                # Assume default date if not specified in the JSON string context, or use a placeholder
                slots_data.append({
                    "service_id": svc_id,
                    "start": start_time,
                    "end": end_time,
                    "date": None  # Will be set dynamically during booking logic
                })

        return {
            "services": services_data,
            "clients": clients_data,
            "slots": slots_data
        }
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        sys.exit(1)
