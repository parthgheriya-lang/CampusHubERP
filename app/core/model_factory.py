
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


class ModelFactory:
    """Factory for creating Student, Faculty, and Course objects."""

    @staticmethod
    def create_model(model_type, **kwargs):
        model_type = model_type.lower()

        if model_type == "student":
            return Student(**kwargs)

        elif model_type == "faculty":
            return Faculty(**kwargs)

        elif model_type == "course":
            return Course(**kwargs)

        else:
            raise ValueError(
                f"Unknown model type: {model_type}. "
                "Use student, faculty, or course."
            )
