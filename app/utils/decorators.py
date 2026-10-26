
from functools import wraps
from datetime import datetime


def log_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Completed: {func.__name__}")
        return result

    return wrapper


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()

        result = func(*args, **kwargs)

        end_time = datetime.now()
        elapsed = (end_time - start_time).total_seconds()

        print(f"[TIME] {func.__name__}: {elapsed:.6f} seconds")
        return result

    return wrapper
