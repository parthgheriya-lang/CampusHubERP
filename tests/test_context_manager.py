
from app.utils.context_manager import report_session


def main():
    with report_session():
        print("Generating student report...")
        print("Student report generated successfully.")


if __name__ == "__main__":
    main()
