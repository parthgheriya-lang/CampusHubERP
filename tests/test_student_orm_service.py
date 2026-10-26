
from app.database.orm_connection import initialize_orm_database
from app.services.student_orm_service import StudentORMService


def main():
    initialize_orm_database()
    service = StudentORMService()

    # CREATE
    print("\nCREATE:")
    service.create_student(
        "ST902",
        "Priya",
        20,
        "priya@example.com",
        "Information Technology"
    )

    # READ
    print("\nREAD:")
    print(service.get_student("ST902"))

    # READ ALL
    print("\nREAD ALL:")
    print(service.get_all_students())

    # UPDATE
    print("\nUPDATE:")
    service.update_student("ST902", name="Priya Sharma")
    print(service.get_student("ST902"))

    # DELETE
    print("\nDELETE:")
    service.delete_student("ST902")
    print("AFTER DELETE:", service.get_student("ST902"))


if __name__ == "__main__":
    main()
