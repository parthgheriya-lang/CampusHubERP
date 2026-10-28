
import unittest
from app.api.api_app import app


class TestFacultyAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.faculty_id = "FC777"

        self.client.delete(f"/faculty/{self.faculty_id}")

        response = self.client.post("/faculty", json={
            "faculty_id": self.faculty_id,
            "name": "API Test Faculty",
            "age": 40,
            "email": "faculty777@example.com",
            "department": "Computer Science",
        })
        self.assertEqual(response.status_code, 201, response.json)

    def test_get_faculty(self):
        response = self.client.get(f"/faculty/{self.faculty_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["faculty_id"], self.faculty_id)

    def test_update_faculty(self):
        response = self.client.put(
            f"/faculty/{self.faculty_id}",
            json={"name": "Updated Faculty"},
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/faculty/{self.faculty_id}")
        self.assertEqual(response.json["name"], "Updated Faculty")

    def test_delete_faculty(self):
        response = self.client.delete(f"/faculty/{self.faculty_id}")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/faculty/{self.faculty_id}")
        self.assertEqual(response.status_code, 404)

    def test_missing_faculty_fields(self):
        response = self.client.post("/faculty", json={"name": "Incomplete"})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        self.client.delete(f"/faculty/{self.faculty_id}")


if __name__ == "__main__":
    unittest.main()
