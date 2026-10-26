
from pathlib import Path
from app.utils.serialization import (
    serialize_to_json,
    deserialize_from_json
)


def main():
    student_data = {
        "student_id": "ST101",
        "name": "Rahul",
        "age": 21,
        "email": "rahul@example.com",
        "department": "Computer Science"
    }

    file_path = Path("data") / "student_data.json"

    # Serialize Python data into JSON
    serialize_to_json(student_data, file_path)

    # Deserialize JSON back into Python data
    loaded_data = deserialize_from_json(file_path)

    print("LOADED DATA:", loaded_data)
    print("DATA MATCH:", loaded_data == student_data)


if __name__ == "__main__":
    main()
