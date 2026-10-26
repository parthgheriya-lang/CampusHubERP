
import unittest
from app.services.course_service import CourseService
from app.models.course import Course


class TestCourse(unittest.TestCase):

    def setUp(self):
        self.service = CourseService()
        self.course_code = "CT999"

    def tearDown(self):
        try:
            self.service.delete_course(self.course_code)
        except (ValueError, KeyError):
            pass

    def create_test_course(self):
        course = Course("CT999", "Test Course", 3)
        self.service.create_course(course)

    def test_add_course(self):
        self.create_test_course()
        course = self.service.get_course("CT999")
        self.assertIsNotNone(course)

    def test_search_course(self):
        self.create_test_course()
        course = self.service.get_course("CT999")
        self.assertIsNotNone(course)

    def test_update_course(self):
        self.create_test_course()
        self.service.update_course("CT999", course_name="Updated Course")
        course = self.service.get_course("CT999")
        self.assertEqual(course.course_name, "Updated Course")

    def test_delete_course(self):
        self.create_test_course()
        self.service.delete_course("CT999")
        self.assertIsNone(self.service.get_course("CT999"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
