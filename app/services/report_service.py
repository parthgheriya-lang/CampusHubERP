
import json
from pathlib import Path
from datetime import datetime


class ReportService:

    def __init__(self):
        self.reports_dir = Path(__file__).resolve().parents[2] / "reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def generate_student_report(self, students):
        report_data = {
            "report_title": "CampusHub ERP - Student Report",
            "generated_at": datetime.now().isoformat(),
            "total_students": len(students),
            "students": [student.to_dict() for student in students],
        }

        filename = (
            "student_report_"
            + datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".json"
        )

        file_path = self.reports_dir / filename

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=4)

        print(f"Report generated: {file_path}")
        return file_path
