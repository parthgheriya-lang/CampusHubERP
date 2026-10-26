
from app.database.connection import initialize_database
from app.services.student_db_service import StudentDBService


def main():
    initialize_database()
    service = StudentDBService()

    # CREATE
    service.create_student(
        "ST901",
        "Rahul",
        21,
        "rahul@example.com",
        "Computer Science"
    )

    # READ
    print("\nREAD STUDENT:")
    print(service.get_student("ST901"))

    # READ ALL
    print("\nREAD ALL STUDENTS:")
    print(service.get_all_students())

    # UPDATE
    print("\nUPDATE STUDENT:")
    service.update_student("ST901", name="Rahul Sharma")
    print(service.get_student("ST901"))

    # DELETE
    print("\nDELETE STUDENT:")
    service.delete_student("ST901")
    print("AFTER DELETE:", service.get_student("ST901"))


if __name__ == "__main__":
    main()
