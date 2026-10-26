
import json
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError

BASE_URL = "http://127.0.0.1:5000"


def api_request(path, method="GET", data=None):
    body = json.dumps(data).encode("utf-8") if data is not None else None

    request = Request(
        BASE_URL + path,
        data=body,
        method=method,
        headers={"Content-Type": "application/json"},
    )

    with urlopen(request, timeout=5) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body) if response_body else {}
        return response.status, result


class TestStudentAPI(unittest.TestCase):

    def setUp(self):
        self.student_id = "ST777"

        # Remove any leftover test record.
        try:
            api_request(f"/students/{self.student_id}", "DELETE")
        except HTTPError as error:
            if error.code != 404:
                raise
            error.close()

        # Create a fresh student for this test.
        status, response = api_request(
            "/students",
            "POST",
            {
                "student_id": self.student_id,
                "name": "API Test Student",
                "age": 20,
                "email": "apitest@example.com",
                "department": "Computer Science",
            },
        )
        self.assertEqual(status, 201, response)

    def test_get_student(self):
        status, student = api_request(
            f"/students/{self.student_id}"
        )
        self.assertEqual(status, 200)
        self.assertEqual(student["student_id"], self.student_id)

    def test_update_student(self):
        status, response = api_request(
            f"/students/{self.student_id}",
            "PUT",
            {"name": "Updated API Student"},
        )

        self.assertEqual(status, 200)
        self.assertEqual(
            response["message"],
            "Student updated successfully",
        )

        # Fetch the student to verify the update.
        status, updated_student = api_request(
            f"/students/{self.student_id}"
        )
        self.assertEqual(status, 200)
        self.assertEqual(
            updated_student["name"],
            "Updated API Student",
        )

    def test_delete_student(self):
        status, response = api_request(
            f"/students/{self.student_id}",
            "DELETE",
        )
        self.assertEqual(status, 200)
        self.assertEqual(
            response["message"],
            "Student deleted successfully",
        )

        with self.assertRaises(HTTPError) as error:
            api_request(f"/students/{self.student_id}")

        self.assertEqual(error.exception.code, 404)
        error.exception.close()

    def tearDown(self):
        # Clean up the test record after each test.
        try:
            api_request(f"/students/{self.student_id}", "DELETE")
        except HTTPError as error:
            if error.code != 404:
                raise
            error.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
