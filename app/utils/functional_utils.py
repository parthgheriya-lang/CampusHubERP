
from functools import reduce


def filter_students(students, department):
    return list(
        filter(
            lambda student: student.department == department,
            students,
        )
    )


def get_student_names(students):
    return list(
        map(lambda student: student.name, students)
    )


def calculate_total_credits(courses):
    return reduce(
        lambda total, course: total + course.credits,
        courses,
        0,
    )


def sort_students_by_name(students):
    return sorted(students, key=lambda student: student.name)
