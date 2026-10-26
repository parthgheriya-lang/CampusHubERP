
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM models."""
    pass


class StudentORM(Base):
    """Student table mapped using SQLAlchemy ORM."""

    __tablename__ = "students_orm"

    student_id: Mapped[str] = mapped_column(
        String(20), primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    age: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(150), nullable=False
    )
    department: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    def __repr__(self):
        return (
            f"StudentORM(student_id={self.student_id!r}, "
            f"name={self.name!r}, age={self.age!r}, "
            f"email={self.email!r}, "
            f"department={self.department!r})"
        )
