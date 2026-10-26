
def student_generator(students):
    """Yield student records one at a time."""
    for student in students:
        yield student


def course_generator(courses):
    """Yield course records one at a time."""
    for course in courses:
        yield course
