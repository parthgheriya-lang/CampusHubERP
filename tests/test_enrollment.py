
import unittest

from app.services.enrollment_service import EnrollmentService
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.models.student import Student
from app.models.course import Course


class TestEnrollment(unittest.TestCase):

    def setUp(self):
        self.student_service = StudentService()
        self.course_service = CourseService()

        self.student_service.create_student(
            Student(
                "ST999",
                "Test Student",
                20,
                "test@example.com",
                "Computer Science"
            )
        )

        self.course_service.create_course(
            Course("CT999", "Test Course", 3)
        )

        self.service = EnrollmentService(
            student_service=self.student_service,
            course_service=self.course_service
        )

        self.enrollment_id = "ST999_CT999"

    def tearDown(self):
        self.service.enrollments.clear()

    def create_test_enrollment(self):
        self.service.create_enrollment("ST999", "CT999")

    def test_add_enrollment(self):
        self.create_test_enrollment()
        enrollment = self.service.get_enrollment(self.enrollment_id)
        self.assertIsNotNone(enrollment)

    def test_search_enrollment(self):
        self.create_test_enrollment()
        enrollment = self.service.get_enrollment(self.enrollment_id)
        self.assertIsNotNone(enrollment)

    def test_update_enrollment(self):
        self.create_test_enrollment()

        result = self.service.update_enrollment(
            self.enrollment_id,
            course_code="CT999"
        )

        self.assertEqual(result["course_code"], "CT999")

    def test_delete_enrollment(self):
        self.create_test_enrollment()
        self.service.delete_enrollment(self.enrollment_id)

        enrollment = self.service.get_enrollment(self.enrollment_id)
        self.assertIsNone(enrollment)

    def test_enrollment_with_invalid_student(self):
        with self.assertRaisesRegex(ValueError, "Student not found"):
            self.service.create_enrollment("ST000", "CT999")

    def test_enrollment_with_invalid_course(self):
        with self.assertRaisesRegex(ValueError, "Course not found"):
            self.service.create_enrollment("ST999", "CS000")


if __name__ == "__main__":
    unittest.main(verbosity=2)
