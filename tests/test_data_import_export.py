
from pathlib import Path
from app.utils.data_import_export import (
    export_students,
    import_students
)


def main():
    students = [
        {
            "student_id": "ST101",
            "name": "Rahul",
            "email": "rahul@example.com",
            "department": "Computer Science"
        },
        {
            "student_id": "ST102",
            "name": "Priya",
            "email": "priya@example.com",
            "department": "Information Technology"
        }
    ]

    file_path = Path("data") / "students_export.json"

    # Export student records
    export_students(students, file_path)

    # Import student records
    imported_students = import_students(file_path)

    print("IMPORTED STUDENTS:", imported_students)
    print("DATA MATCH:", imported_students == students)


if __name__ == "__main__":
    main()
