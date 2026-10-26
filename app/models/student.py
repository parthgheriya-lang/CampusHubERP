
from app.core.descriptors import (
    NameDescriptor,
    EmailDescriptor,
    AgeDescriptor,
)
from app.models.person import PersonModel


class Student(PersonModel):
    name = NameDescriptor()
    age = AgeDescriptor()
    email = EmailDescriptor()

    def __init__(
        self, student_id, name, age, email, department
    ):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.department = department

    def display_details(self):
        print("Student Details")
        print("----------------")
        for key, value in self.to_dict().items():
            print(f"{key}: {value}")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
