
from app.models.student import Student
from app.models.course import Course
from app.utils.functional_utils import (
    filter_students,
    get_student_names,
    calculate_total_credits,
    sort_students_by_name,
)


def main():
    students = [
        Student("ST101", "Rahul", 21, "rahul@example.com", "Computer Science"),
        Student("ST102", "Amit", 22, "amit@example.com", "Information Technology"),
        Student("ST103", "Priya", 20, "priya@example.com", "Computer Science"),
    ]

    courses = [
        Course("CS101", "Python Programming", 4),
        Course("CS102", "Database Management", 3),
    ]

    # FILTER
    cs_students = filter_students(students, "Computer Science")
    print("FILTER:", [s.name for s in cs_students])

    # MAP
    print("MAP:", get_student_names(students))

    # REDUCE
    print("REDUCE:", calculate_total_credits(courses))

    # SORT
    print("SORT:", [s.name for s in sort_students_by_name(students)])


if __name__ == "__main__":
    main()
