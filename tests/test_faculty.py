
import unittest
from app.services.faculty_service import FacultyService
from app.models.faculty import Faculty


class TestFaculty(unittest.TestCase):

    def setUp(self):
        self.service = FacultyService()
        self.faculty_id = "FC999"

    def tearDown(self):
        try:
            self.service.delete_faculty(self.faculty_id)
        except ValueError:
            pass

    def create_test_faculty(self):
        faculty = Faculty(
            "FC999",
            "Test Faculty",
            35,
            "faculty@example.com",
            "Computer Science"
        )
        self.service.create_faculty(faculty)

    def test_add_faculty(self):
        self.create_test_faculty()
        faculty = self.service.get_faculty("FC999")
        self.assertIsNotNone(faculty)
        self.assertEqual(faculty.name, "Test Faculty")

    def test_search_faculty(self):
        self.create_test_faculty()
        faculty = self.service.get_faculty("FC999")
        self.assertEqual(faculty.faculty_id, "FC999")

    def test_update_faculty(self):
        self.create_test_faculty()
        self.service.update_faculty(
            "FC999", name="Updated Faculty"
        )
        faculty = self.service.get_faculty("FC999")
        self.assertEqual(faculty.name, "Updated Faculty")

    def test_delete_faculty(self):
        self.create_test_faculty()
        self.service.delete_faculty("FC999")
        self.assertIsNone(self.service.get_faculty("FC999"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
