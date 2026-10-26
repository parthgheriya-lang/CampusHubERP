
from app.utils.decorators import log_operation, measure_time


@log_operation
@measure_time
def calculate_total(a, b):
    return a + b


def main():
    result = calculate_total(10, 20)
    print("Result:", result)


if __name__ == "__main__":
    main()
