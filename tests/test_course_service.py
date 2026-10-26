
from app.models.course import Course
from app.services.course_service import CourseService


def main():
    service = CourseService()

    course = Course("CS201", "Database Management", 4)

    # CREATE
    service.create_course(course)
    print("CREATE:", course.course_code)

    # READ
    found = service.get_course("CS201")
    print("READ:", found.course_name)

    # READ ALL
    print("READ ALL:", len(service.get_all_courses()), "course(s)")

    # UPDATE
    service.update_course(
        "CS201",
        course_name="Advanced Database Management",
    )
    print("UPDATE:", service.get_course("CS201").course_name)

    # DELETE
    deleted = service.delete_course("CS201")
    print("DELETE:", deleted.course_code)

    # VERIFY DELETE
    print("AFTER DELETE:", service.get_course("CS201"))


if __name__ == "__main__":
    main()
