
import json
from pathlib import Path


def export_students(students, file_path):
    """Export student records to a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, default=str)

    print(f"Exported {len(students)} student record(s).")
    return path


def import_students(file_path):
    """Import student records from a JSON file."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        students = json.load(file)

    if not isinstance(students, list):
        raise ValueError("The JSON file must contain a list of students.")

    print(f"Imported {len(students)} student record(s).")
    return students
