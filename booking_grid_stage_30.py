# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: BookingGrid
class Profile:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role  # "admin", "staff", "client"

    @classmethod
    def load_profiles(cls):
        profiles_path = os.path.join(DATA_DIR, "profiles.json")
        if not os.path.exists(profiles_path):
            return [cls("Организатор", "admin"), cls("Администратор", "staff")]
        with open(profiles_path) as f:
            data = json.load(f)
        return [cls(p["name"], p.get("role", "user")) for p in data]

    def save_profiles(self):
        profiles_path = os.path.join(DATA_DIR, "profiles.json")
        data = [{"name": self.name, "role": self.role} for _, self_ in enumerate([self])]
        with open(profiles_path, "w") as f:
            json.dump(data, f, indent=2)

# Глобальный список профилей
PROFILES = Profile.load_profiles()


def get_profile(name):
    """Возвращает профиль по имени или None."""
    for p in PROFILES:
        if p.name == name or p.role == "admin":
            return p
    return None


def create_profile():
    print("Создание нового профиля.")
    name = input("Имя профиля: ").strip()
    role = input("Роль (user/staff/admin): ").strip().lower() or "user"
    if get_profile(name):
        print(f"Профиль '{name}' уже существует.")
        return None
    p = Profile(name, role)
    PROFILES.append(p)
    p.save_profiles()
    print(f"Профиль '{p.name}' ({p.role}) создан.")
    return p


def list_profiles():
    for i, p in enumerate(PROFILES):
        print(f"{i+1}. {p.name} — {p.role}")


def switch_profile(name=None):
    """Переключить на профиль по имени или индексу (0-based)."""
    if name is not None:
        return get_profile(name)
    idx_str = input("Введите индекс профиля (или 0 для дефолта): ").strip() or "0"
    try:
        idx = int(idx_str) % len(PROFILES)
        current = PROFILES[idx]
        print(f"Переключение на профиль: {current.name} ({current.role})")
        return current
    except (ValueError, IndexError):
        print("Неверный индекс.")
        return None


if __name__ == "__main__":
    while True:
        cmd = input("\n[pro]files [list|create|switch|exit]: ").strip().lower()
        if cmd in ("exit", "quit"):
            break
        elif cmd == "list":
            list_profiles()
        elif cmd == "create":
            create_profile()
        elif cmd.startswith("switch"):
            name = input("Имя профиля для переключения: ").strip() or None
            switch_profile(name)
