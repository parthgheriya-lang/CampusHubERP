
import sqlite3

from app.database.student_repository import StudentRepository
from app.utils.logger import (
    logger,
    log_student_added,
    log_student_updated,
    log_student_deleted,
)
from app.utils.validators import validate_email


class StudentDBService:
    """Manage student records through the repository layer."""

    def __init__(self, repository=None):
        self.repository = repository or StudentRepository()

    def create_student(self, student_id, name, age, email, department):
        if not validate_email(email):
            logger.warning(
                "Invalid email provided for student: %s", student_id
            )
            raise ValueError("Invalid email address.")

        try:
            self.repository.add(
                student_id, name, age, email, department
            )
        except sqlite3.IntegrityError as error:
            logger.warning(
                "Duplicate student ID attempted: %s", student_id
            )
            raise ValueError(
                f"Student ID already exists: {student_id}"
            ) from error

        log_student_added(student_id)
        print(f"Student created: {student_id}")

    def get_student(self, student_id):
        return self.repository.get_by_id(student_id)

    def get_all_students(self):
        return self.repository.get_all()

    def update_student(self, student_id, **updates):
        allowed_fields = {"name", "age", "email", "department"}

        fields = {
            key: value
            for key, value in updates.items()
            if key in allowed_fields
        }

        if not fields:
            print("No valid fields provided for update.")
            return False

        if "email" in fields and not validate_email(fields["email"]):
            logger.warning(
                "Invalid email provided for student: %s", student_id
            )
            raise ValueError("Invalid email address.")

        updated_student = self.repository.update(student_id, **fields)

        if updated_student is not None:
            log_student_updated(student_id)
            print(f"Student updated: {student_id}")
            return True

        logger.warning("Student not found for update: %s", student_id)
        print(f"Student not found: {student_id}")
        return False

    def delete_student(self, student_id):
        deleted = self.repository.delete(student_id)

        if deleted:
            log_student_deleted(student_id)
            print(f"Student deleted: {student_id}")
            return True

        logger.warning("Student not found for deletion: %s", student_id)
        print(f"Student not found: {student_id}")
        return False
