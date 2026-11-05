# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: BookingGrid
import json
from datetime import datetime

class FavoritesManager:
    def __init__(self, data):
        self.data = data
        self.favorites = []

    def add_favorite(self, booking):
        if booking not in self.favorites:
            self.favorites.append(booking)
            return True
        return False

    def remove_favorite(self, booking):
        if booking in self.favorites:
            self.favorites.remove(booking)
            return True
        return False

    def get_favorites(self):
        return self.favorites

    def load_favorites(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                self.favorites = json.load(f)

    def save_favorites(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.favorites, f, ensure_ascii=False, indent=2)

    def quick_access(self, booking):
        for fav in self.favorites:
            if fav == booking:
                return True
        return False
