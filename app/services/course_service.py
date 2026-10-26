
from app.utils.logger import logger, log_course_added


class CourseService:
    """Manage course records."""

    def __init__(self):
        self.courses = {}

    # CREATE
    def create_course(self, course):
        if course.course_code in self.courses:
            raise ValueError("Course already exists.")

        self.courses[course.course_code] = course

        log_course_added(course.course_code)
        return course

    # READ
    def get_course(self, course_code):
        return self.courses.get(course_code)

    def get_all_courses(self):
        return list(self.courses.values())

    # UPDATE
    def update_course(self, course_code, **updates):
        course = self.get_course(course_code)

        if course is None:
            raise ValueError("Course not found.")

        allowed_fields = {
            "course_name", "credits"
        }

        for field, value in updates.items():
            if field not in allowed_fields:
                raise ValueError(f"Invalid field: {field}")

            setattr(course, field, value)

        course.update_timestamp()
        logger.info("Course Updated: %s", course_code)
        return course

    # DELETE
    def delete_course(self, course_code):
        if course_code not in self.courses:
            raise ValueError("Course not found.")

        course = self.courses.pop(course_code)
        logger.info("Course Deleted: %s", course_code)
        return course
