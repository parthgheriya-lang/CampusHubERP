
from app.models.student import Student
from app.models.course import Course
from app.utils.generators import student_generator, course_generator


def main():
    students = [
        Student("ST101", "Rahul", 21, "rahul@example.com", "Computer Science"),
        Student("ST102", "Priya", 20, "priya@example.com", "Information Technology"),
    ]

    courses = [
        Course("CS101", "Python Programming", 4),
        Course("CS102", "Database Management", 3),
    ]

    print("STUDENT GENERATOR:")
    for student in student_generator(students):
        print(student.student_id, "-", student.name)

    print("\nCOURSE GENERATOR:")
    for course in course_generator(courses):
        print(course.course_code, "-", course.course_name)


if __name__ == "__main__":
    main()
