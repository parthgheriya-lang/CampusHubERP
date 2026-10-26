
import multiprocessing
import os


def process_student(student):
    """Process a student record in a separate process."""
    print(
        f"[Process ID: {os.getpid()}] "
        f"Processing student: {student}"
    )
    return f"Completed processing student: {student}"


def process_students_parallel(students):
    """Process student records using multiple processes."""
    if not students:
        print("No student records to process.")
        return []

    with multiprocessing.Pool() as pool:
        results = pool.map(process_student, students)

    for result in results:
        print(result)

    print("All student records processed successfully.")
    return results
