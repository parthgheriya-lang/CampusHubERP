
from app.database.connection import get_connection


class StudentRepository:
    """Handle database CRUD operations for students."""

    def add(self, student_id, name, age, email, department):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO students
                (student_id, name, age, email, department)
                VALUES (?, ?, ?, ?, ?)
                """,
                (student_id, name, age, email, department),
            )
        return self.get_by_id(student_id)

    def get_by_id(self, student_id):
        with get_connection() as connection:
            row = connection.execute(
                "SELECT * FROM students WHERE student_id = ?",
                (student_id,),
            ).fetchone()
        return dict(row) if row else None

    def get_all(self):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT * FROM students ORDER BY student_id"
            ).fetchall()
        return [dict(row) for row in rows]

    def update(self, student_id, **updates):
        allowed_fields = {"name", "age", "email", "department"}

        for field in updates:
            if field not in allowed_fields:
                raise ValueError(f"Invalid field: {field}")

        if not updates:
            return self.get_by_id(student_id)

        assignments = ", ".join(
            f"{field} = ?" for field in updates
        )
        values = list(updates.values()) + [student_id]

        with get_connection() as connection:
            cursor = connection.execute(
                f"UPDATE students SET {assignments} WHERE student_id = ?",
                values,
            )

        if cursor.rowcount == 0:
            return None

        return self.get_by_id(student_id)

    def delete(self, student_id):
        with get_connection() as connection:
            cursor = connection.execute(
                "DELETE FROM students WHERE student_id = ?",
                (student_id,),
            )
        return cursor.rowcount > 0
