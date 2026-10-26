
import re

from app.core.metaclasses import BaseModel


class Course(BaseModel):

    def __init__(self, course_code, course_name, credits):
        super().__init__()

        if not isinstance(course_code, str) or not re.fullmatch(
            r"[A-Z]{2}\d{3}", course_code
        ):
            raise ValueError(
                "Invalid Course Code. Use two uppercase letters "
                "followed by three digits, e.g. CS101."
            )

        if not course_name or not course_name.strip():
            raise ValueError("Course name cannot be empty.")

        if not isinstance(credits, int) or credits <= 0:
            raise ValueError("Credits must be a positive integer.")

        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def display_details(self):
        print("Course Details")
        print("----------------")
        for key, value in self.to_dict().items():
            print(f"{key}: {value}")

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
