# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: BookingGrid
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.active_profile_id = None

    def add_profile(self, name, user_id=None, password=None):
        profile_id = len(self.profiles) + 1 if self.profiles else 0
        self.profiles[profile_id] = {
            'name': name,
            'user_id': user_id,
            'password': password or ''
        }
        return profile_id

    def switch_profile(self, target_id):
        if target_id not in self.profiles:
            raise ValueError(f"Профиль с ID {target_id} не найден")
        self.active_profile_id = target_id

    def get_current_user_id(self):
        if self.active_profile_id is None:
            return None
        profile = self.profiles[self.active_profile_id]
        return profile['user_id']

    def login(self, user_id=None, password=None):
        if user_id is not None and password is not None:
            for pid, p in self.profiles.items():
                if p['user_id'] == user_id and p['password'] == password:
                    return pid
        return None

    def logout(self):
        self.active_profile_id = None
