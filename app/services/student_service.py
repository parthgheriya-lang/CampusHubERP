
class StudentService:

    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student already exists.")

        self.students[student.student_id] = student
        return student

    # READ
    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())

    # UPDATE
    def update_student(self, student_id, **updates):
        student = self.get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        allowed_fields = {
            "name", "age", "email", "department"
        }

        for field, value in updates.items():
            if field not in allowed_fields:
                raise ValueError(f"Invalid field: {field}")

            setattr(student, field, value)

        student.update_timestamp()
        return student

    # DELETE
    def delete_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found.")

        return self.students.pop(student_id)
