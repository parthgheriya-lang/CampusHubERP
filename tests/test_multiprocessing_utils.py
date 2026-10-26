
from app.utils.multiprocessing_utils import process_students_parallel


def main():
    students = [
        "ST101 - Rahul",
        "ST102 - Priya",
        "ST103 - Amit"
    ]

    print("Starting parallel student processing...")
    process_students_parallel(students)


if __name__ == "__main__":
    main()
