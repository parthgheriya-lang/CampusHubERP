
import asyncio


async def process_student(student):
    """Process a student asynchronously."""
    print(f"Starting student processing: {student}")

    # Simulate an asynchronous operation
    await asyncio.sleep(1)

    print(f"Completed student processing: {student}")
    return f"Processed: {student}"


async def process_students_async(students):
    """Process multiple students concurrently using asyncio."""
    tasks = [
        process_student(student)
        for student in students
    ]

    results = await asyncio.gather(*tasks)

    print("All student records processed successfully.")
    return results
