
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.student_orm import Base


DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "campushub.db"
)

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)


def initialize_orm_database():
    """Create ORM tables if they do not already exist."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)
    print("SQLAlchemy ORM database initialized successfully.")
    print(f"Database location: {DATABASE_PATH}")


def get_session():
    """Return a new SQLAlchemy database session."""
    return SessionLocal()


if __name__ == "__main__":
    initialize_orm_database()
