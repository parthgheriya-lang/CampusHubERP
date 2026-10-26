
from app.utils.threading_utils import process_students_concurrently


def main():
    students = ["ST101 - Rahul", "ST102 - Priya", "ST103 - Amit"]

    print("Starting student processing...")
    process_students_concurrently(students)


if __name__ == "__main__":
    main()
