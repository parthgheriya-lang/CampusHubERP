
import json
from pathlib import Path


def serialize_to_json(data, file_path):
    """Save Python data as a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, default=str)

    print(f"Data saved to JSON: {path}")
    return path


def deserialize_from_json(file_path):
    """Load data from a JSON file."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Data loaded from JSON: {path}")
    return data
