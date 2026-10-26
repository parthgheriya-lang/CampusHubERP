
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


def main():
    student = Student(
        "ST001",
        "Parth",
        20,
        "parth@example.com",
        "Computer Science",
    )

    faculty = Faculty(
        "FC001",
        "Amit Sharma",
        40,
        "amit@example.com",
        "Computer Science",
    )

    course = Course(
        "CS101",
        "Python Programming",
        4,
    )

    print("\n=== STUDENT ===")
    student.display_details()

    print("\n=== FACULTY ===")
    faculty.display_details()

    print("\n=== COURSE ===")
    course.display_details()


if __name__ == "__main__":
    main()

    
    print("\n=== DESCRIPTOR VALIDATION TEST ===")

    try:
        Student(
            "ST002",
            "",
            20,
            "test@example.com",
            "Computer Science",
        )
    except ValueError as error:
        print("Validation working:", error)


    try:
        Student(
            "ST003",
            "Test Student",
            20,
            "invalid-email",
            "Computer Science",
        )
    except ValueError as error:
        print("Email validation working:", error)

    try:
        Student(
            "ST004",
            "Test Student",
            15,
            "test@example.com",
            "Computer Science",
        )
    except ValueError as error:
        print("Age validation working:", error)

