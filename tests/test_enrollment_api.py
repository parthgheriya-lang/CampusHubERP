
import unittest
from app.api.api_app import app


class TestEnrollmentAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.student_id = "ST778"
        self.course_code = "CS778"
        self.enrollment_id = f"{self.student_id}_{self.course_code}"

        # Remove leftover test records.
        self.client.delete(f"/enrollments/{self.enrollment_id}")
        self.client.delete(f"/students/{self.student_id}")
        self.client.delete(f"/courses/{self.course_code}")

        student_response = self.client.post("/students", json={
            "student_id": self.student_id,
            "name": "Enrollment API Student",
            "age": 20,
            "email": "enrollment778@example.com",
            "department": "Computer Science",
        })
        self.assertEqual(student_response.status_code, 201, student_response.json)

        course_response = self.client.post("/courses", json={
            "course_code": self.course_code,
            "course_name": "Enrollment API Course",
            "credits": 3,
        })
        self.assertEqual(course_response.status_code, 201, course_response.json)

        enrollment_response = self.client.post("/enrollments", json={
            "student_id": self.student_id,
            "course_code": self.course_code,
        })
        self.assertEqual(enrollment_response.status_code, 201, enrollment_response.json)

    def test_get_enrollment(self):
        response = self.client.get(f"/enrollments/{self.enrollment_id}")
        self.assertEqual(response.status_code, 200)

    def test_update_enrollment(self):
        response = self.client.put(
            f"/enrollments/{self.enrollment_id}",
            json={"course_code": self.course_code},
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_enrollment(self):
        response = self.client.delete(f"/enrollments/{self.enrollment_id}")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/enrollments/{self.enrollment_id}")
        self.assertEqual(response.status_code, 404)

    def test_missing_enrollment_fields(self):
        response = self.client.post("/enrollments", json={})
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        self.client.delete(f"/enrollments/{self.enrollment_id}")
        self.client.delete(f"/students/{self.student_id}")
        self.client.delete(f"/courses/{self.course_code}")


if __name__ == "__main__":
    unittest.main()
