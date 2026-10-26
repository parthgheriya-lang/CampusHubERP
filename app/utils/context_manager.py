
from contextlib import contextmanager
from datetime import datetime


@contextmanager
def report_session():
    print("Opening report session...")
    start_time = datetime.now()

    try:
        yield
    finally:
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print("Closing report session...")
        print(f"Session duration: {duration:.6f} seconds")
