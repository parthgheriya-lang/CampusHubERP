
from app.models.faculty import Faculty
from app.services.faculty_service import FacultyService


def main():
    service = FacultyService()

    faculty = Faculty(
        "FC101",
        "Amit Sharma",
        40,
        "amit@example.com",
        "Computer Science",
    )

    # CREATE
    service.create_faculty(faculty)
    print("CREATE:", faculty.faculty_id)

    # READ
    found = service.get_faculty("FC101")
    print("READ:", found.name)

    # READ ALL
    print("READ ALL:", len(service.get_all_faculty()), "faculty member(s)")

    # UPDATE
    service.update_faculty("FC101", name="Amit Kumar")
    print("UPDATE:", service.get_faculty("FC101").name)

    # DELETE
    deleted = service.delete_faculty("FC101")
    print("DELETE:", deleted.faculty_id)

    # VERIFY DELETE
    print("AFTER DELETE:", service.get_faculty("FC101"))


if __name__ == "__main__":
    main()
