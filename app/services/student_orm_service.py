
from app.database.orm_connection import get_session
from app.models.student_orm import StudentORM


class StudentORMService:
    """Manage student records using SQLAlchemy ORM."""

    def create_student(self, student_id, name, age, email, department):
        with get_session() as session:
            try:
                student = StudentORM(
                    student_id=student_id,
                    name=name,
                    age=age,
                    email=email,
                    department=department
                )
                session.add(student)
                session.commit()
                print(f"Student created: {student_id}")
                return student
            except Exception:
                session.rollback()
                raise

    def get_student(self, student_id):
        with get_session() as session:
            return session.get(StudentORM, student_id)

    def get_all_students(self):
        with get_session() as session:
            return session.query(StudentORM).order_by(
                StudentORM.student_id
            ).all()

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

        with get_session() as session:
            try:
                student = session.get(StudentORM, student_id)

                if student is None:
                    print(f"Student not found: {student_id}")
                    return False

                for field, value in fields.items():
                    setattr(student, field, value)

                session.commit()
                print(f"Student updated: {student_id}")
                return True
            except Exception:
                session.rollback()
                raise

    def delete_student(self, student_id):
        with get_session() as session:
            try:
                student = session.get(StudentORM, student_id)

                if student is None:
                    print(f"Student not found: {student_id}")
                    return False

                session.delete(student)
                session.commit()
                print(f"Student deleted: {student_id}")
                return True
            except Exception:
                session.rollback()
                raise
