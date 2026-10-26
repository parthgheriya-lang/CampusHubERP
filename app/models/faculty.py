
from app.core.descriptors import (
    NameDescriptor,
    EmailDescriptor,
    AgeDescriptor,
)
from app.models.person import PersonModel


class Faculty(PersonModel):
    name = NameDescriptor()
    age = AgeDescriptor()
    email = EmailDescriptor()

    def __init__(
        self, faculty_id, name, age, email, department
    ):
        super().__init__(name, age, email)
        self.faculty_id = faculty_id
        self.department = department

    def display_details(self):
        print("Faculty Details")
        print("----------------")
        for key, value in self.to_dict().items():
            print(f"{key}: {value}")

    def to_dict(self):
        return {
            "faculty_id": self.faculty_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
