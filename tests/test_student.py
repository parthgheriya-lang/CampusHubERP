
import unittest
from app.services.student_db_service import StudentDBService
from app.database.connection import initialize_database, get_connection


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_database()
        cls.service = StudentDBService()

    def setUp(self):
        # Keep tests independent by removing the test record first.
        with get_connection() as connection:
            connection.execute(
                "DELETE FROM students WHERE student_id = ?",
                ("ST999",)
            )

    def tearDown(self):
        with get_connection() as connection:
            connection.execute(
                "DELETE FROM students WHERE student_id = ?",
                ("ST999",)
            )

    def test_add_student(self):
        self.service.create_student(
            "ST999", "Test Student", 20,
            "test@example.com", "Computer Science"
        )
        student = self.service.get_student("ST999")
        self.assertIsNotNone(student)
        self.assertEqual(student["name"], "Test Student")

    def test_search_student(self):
        self.service.create_student(
            "ST999", "Test Student", 20,
            "test@example.com", "Computer Science"
        )
        student = self.service.get_student("ST999")
        self.assertEqual(student["student_id"], "ST999")

    def test_update_student(self):
        self.service.create_student(
            "ST999", "Test Student", 20,
            "test@example.com", "Computer Science"
        )
        result = self.service.update_student(
            "ST999", name="Updated Student"
        )
        student = self.service.get_student("ST999")
        self.assertTrue(result)
        self.assertEqual(student["name"], "Updated Student")

    def test_delete_student(self):
        self.service.create_student(
            "ST999", "Test Student", 20,
            "test@example.com", "Computer Science"
        )
        result = self.service.delete_student("ST999")
        self.assertTrue(result)
        self.assertIsNone(self.service.get_student("ST999"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
