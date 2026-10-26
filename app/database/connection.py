
import sqlite3
from pathlib import Path


DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "campushub.db"
)


class DatabaseConnection:
    """Singleton manager for the SQLite database connection."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def get_connection(self):
        """Return the shared SQLite connection."""
        DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

        if self._connection is None:
            self._connection = sqlite3.connect(
                DATABASE_PATH,
                check_same_thread=False
            )
            self._connection.row_factory = sqlite3.Row

        return self._connection

    def close_connection(self):
        """Close the shared connection."""
        if self._connection is not None:
            self._connection.close()
            self._connection = None


_database = DatabaseConnection()


def get_connection():
    """Return the shared SQLite connection."""
    return _database.get_connection()


def initialize_database():
    """Create the students table if it does not exist."""
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)

    connection.commit()

    print("Database initialized successfully.")
    print(f"Database location: {DATABASE_PATH}")


if __name__ == "__main__":
    initialize_database()
