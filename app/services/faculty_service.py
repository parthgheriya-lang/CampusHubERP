
from app.utils.logger import log_faculty_added
from app.utils.logger import logger


class FacultyService:
    """Manage faculty records."""

    def __init__(self):
        self.faculty_members = {}

    # CREATE
    def create_faculty(self, faculty):
        if faculty.faculty_id in self.faculty_members:
            raise ValueError("Faculty already exists.")

        self.faculty_members[faculty.faculty_id] = faculty

        log_faculty_added(faculty.faculty_id)
        return faculty

    # READ
    def get_faculty(self, faculty_id):
        return self.faculty_members.get(faculty_id)

    def get_all_faculty(self):
        return list(self.faculty_members.values())

    # UPDATE
    def update_faculty(self, faculty_id, **updates):
        faculty = self.get_faculty(faculty_id)

        if faculty is None:
            raise ValueError("Faculty not found.")

        allowed_fields = {
            "name", "age", "email", "department"
        }

        for field, value in updates.items():
            if field not in allowed_fields:
                raise ValueError(f"Invalid field: {field}")

            setattr(faculty, field, value)

        faculty.update_timestamp()
        logger.info("Faculty Updated: %s", faculty_id)
        return faculty

    # DELETE
    def delete_faculty(self, faculty_id):
        if faculty_id not in self.faculty_members:
            raise ValueError("Faculty not found.")

        faculty = self.faculty_members.pop(faculty_id)
        logger.info("Faculty Deleted: %s", faculty_id)
        return faculty
