
import unittest
from app.api.api_app import app


class TestCourseAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.course_code = "CS777"

        self.client.delete(f"/courses/{self.course_code}")

        response = self.client.post("/courses", json={
            "course_code": self.course_code,
            "course_name": "API Test Course",
            "credits": 3,
        })
        self.assertEqual(response.status_code, 201, response.json)

    def test_get_course(self):
        response = self.client.get(f"/courses/{self.course_code}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["course_code"], self.course_code)

    def test_update_course(self):
        response = self.client.put(
            f"/courses/{self.course_code}",
            json={"course_name": "Updated API Course"},
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/courses/{self.course_code}")
        self.assertEqual(response.json["course_name"], "Updated API Course")

    def test_delete_course(self):
        response = self.client.delete(f"/courses/{self.course_code}")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/courses/{self.course_code}")
        self.assertEqual(response.status_code, 404)

    def test_missing_course_fields(self):
        response = self.client.post("/courses", json={"course_name": "Incomplete"})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        self.client.delete(f"/courses/{self.course_code}")


if __name__ == "__main__":
    unittest.main()
