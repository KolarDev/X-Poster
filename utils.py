import json
import os

def load_json(file_path, default_value=None):
    """Safely loads a JSON file or returns a default value if not found."""
    if not os.path.exists(file_path):
        return default_value if default_value is not None else []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file_path, data):
    """Saves data to a JSON file with pretty formatting."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)