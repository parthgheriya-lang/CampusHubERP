
import threading
import time


def process_student(student):
    """Process an individual student record."""
    print(
        f"[{threading.current_thread().name}] "
        f"Processing student: {student}"
    )
    time.sleep(1)
    print(f"Completed processing student: {student}")


def process_students_concurrently(students):
    """Process multiple student records using threads."""
    threads = []

    for student in students:
        thread = threading.Thread(
            target=process_student,
            args=(student,)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All student records processed successfully.")
