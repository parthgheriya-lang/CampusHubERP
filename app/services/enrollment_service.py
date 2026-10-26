
from app.utils.logger import logger, log_enrollment_created


class EnrollmentService:
    """Manage student course enrollments."""

    def __init__(self, student_service=None, course_service=None):
        self.enrollments = {}
        self.student_service = student_service
        self.course_service = course_service

    def _validate_student_and_course(self, student_id, course_code):
        # Validate student when a StudentService is provided.
        if self.student_service is not None:
            if self.student_service.get_student(student_id) is None:
                logger.warning("Enrollment failed: Student not found: %s", student_id)
                raise ValueError(f"Student not found: {student_id}")

        # Validate course when a CourseService is provided.
        if self.course_service is not None:
            if self.course_service.get_course(course_code) is None:
                logger.warning("Enrollment failed: Course not found: %s", course_code)
                raise ValueError(f"Course not found: {course_code}")

    # CREATE
    def create_enrollment(self, student_id, course_code):
        self._validate_student_and_course(student_id, course_code)

        enrollment_id = f"{student_id}_{course_code}"

        if enrollment_id in self.enrollments:
            raise ValueError("Enrollment already exists.")

        enrollment = {
            "enrollment_id": enrollment_id,
            "student_id": student_id,
            "course_code": course_code,
        }

        self.enrollments[enrollment_id] = enrollment
        log_enrollment_created(student_id, course_code)
        return enrollment

    # READ
    def get_enrollment(self, enrollment_id):
        return self.enrollments.get(enrollment_id)

    def get_all_enrollments(self):
        return list(self.enrollments.values())

    # UPDATE
    def update_enrollment(self, enrollment_id, **updates):
        enrollment = self.get_enrollment(enrollment_id)

        if enrollment is None:
            raise ValueError("Enrollment not found.")

        allowed_fields = {"student_id", "course_code"}

        for field in updates:
            if field not in allowed_fields:
                raise ValueError(f"Invalid field: {field}")

        new_student_id = updates.get(
            "student_id", enrollment["student_id"]
        )
        new_course_code = updates.get(
            "course_code", enrollment["course_code"]
        )

        self._validate_student_and_course(
            new_student_id, new_course_code
        )

        new_id = f"{new_student_id}_{new_course_code}"

        if new_id != enrollment_id and new_id in self.enrollments:
            raise ValueError("Enrollment already exists.")

        updated = {
            "enrollment_id": new_id,
            "student_id": new_student_id,
            "course_code": new_course_code,
        }

        del self.enrollments[enrollment_id]
        self.enrollments[new_id] = updated

        logger.info("Enrollment Updated: %s", new_id)
        return updated

    # DELETE
    def delete_enrollment(self, enrollment_id):
        if enrollment_id not in self.enrollments:
            raise ValueError("Enrollment not found.")

        enrollment = self.enrollments.pop(enrollment_id)
        logger.info("Enrollment Deleted: %s", enrollment_id)
        return enrollment
