
from app.models.student import Student
from app.services.student_service import StudentService


def main():
    service = StudentService()

    student = Student(
        "ST101",
        "Rahul",
        21,
        "rahul@example.com",
        "Computer Science",
    )

    # CREATE
    service.create_student(student)
    print("CREATE:", student.student_id)

    # READ
    found = service.get_student("ST101")
    print("READ:", found.name)

    # READ ALL
    print("READ ALL:", len(service.get_all_students()), "student(s)")

    # UPDATE
    service.update_student("ST101", name="Rahul Sharma")
    print("UPDATE:", service.get_student("ST101").name)

    # DELETE
    deleted = service.delete_student("ST101")
    print("DELETE:", deleted.student_id)

    # VERIFY DELETE
    print("AFTER DELETE:", service.get_student("ST101"))


if __name__ == "__main__":
    main()
