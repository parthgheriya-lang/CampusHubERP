
from app.services.enrollment_service import EnrollmentService


def main():
    service = EnrollmentService()

    # CREATE
    enrollment = service.create_enrollment("ST101", "CS201")
    print("CREATE:", enrollment)

    # READ
    found = service.get_enrollment("ST101_CS201")
    print("READ:", found)

    # READ ALL
    print("READ ALL:", len(service.get_all_enrollments()))

    # UPDATE
    updated = service.update_enrollment(
        "ST101_CS201",
        course_code="CS202",
    )
    print("UPDATE:", updated)

    # DELETE
    deleted = service.delete_enrollment("ST101_CS202")
    print("DELETE:", deleted)

    # VERIFY DELETE
    print("AFTER DELETE:", service.get_enrollment("ST101_CS202"))


if __name__ == "__main__":
    main()
