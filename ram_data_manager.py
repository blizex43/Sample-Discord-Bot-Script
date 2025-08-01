# ram_data_manager.py
# Custom module for loading and saving bot data

import json
import os

class DataManager:
    def __init__(self, filename):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        """Creates the data file if it doesn't exist"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({"blacklist": [], "auth_keys": ["defaultkey"], "config": {}}, f)

    def load(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def get_data(self, key):
        data = self.load()
        return data.get(key)

    def save_data(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)
