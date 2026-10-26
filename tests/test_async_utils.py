
import asyncio
from app.utils.async_utils import process_students_async


async def main():
    students = [
        "ST101 - Rahul",
        "ST102 - Priya",
        "ST103 - Amit"
    ]

    print("Starting asynchronous student processing...")

    results = await process_students_async(students)

    print("RESULTS:", results)


if __name__ == "__main__":
    asyncio.run(main())
