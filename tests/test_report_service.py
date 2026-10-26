
from app.models.student import Student
from app.services.report_service import ReportService


def main():
    students = [
        Student(
            "ST201",
            "Rahul",
            21,
            "rahul@example.com",
            "Computer Science"
        ),
        Student(
            "ST202",
            "Priya",
            20,
            "priya@example.com",
            "Information Technology"
        ),
    ]

    service = ReportService()
    report_path = service.generate_student_report(students)

    print("REPORT EXISTS:", report_path.exists())
    print("REPORT FILE:", report_path.name)


if __name__ == "__main__":
    main()
