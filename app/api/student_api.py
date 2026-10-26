
from flask import Flask, jsonify, request
from app.services.student_orm_service import StudentORMService
from app.database.orm_connection import initialize_orm_database

app = Flask(__name__)
student_service = StudentORMService()

# Initialize the database
initialize_orm_database()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to CampusHub ERP Student API"
    })


@app.route("/students", methods=["GET"])
def get_students():
    students = student_service.get_all_students()
    return jsonify([
        {
            "student_id": s.student_id,
            "name": s.name,
            "age": s.age,
            "email": s.email,
            "department": s.department
        }
        for s in students
    ])


@app.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):
    student = student_service.get_student(student_id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "department": student.department
    })


@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json(silent=True) or {}

    required = ["student_id", "name", "age", "email", "department"]
    if any(field not in data for field in required):
        return jsonify({"error": "All student fields are required"}), 400

    try:
        student = student_service.create_student(
            data["student_id"],
            data["name"],
            int(data["age"]),
            data["email"],
            data["department"]
        )
        return jsonify({
            "message": "Student created successfully",
            "student_id": student.student_id
        }), 201
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be a valid integer"}), 400
    except Exception:
        return jsonify({
            "error": "Could not create student. Check whether the ID already exists."
        }), 400


@app.route("/students/<student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True) or {}
    allowed = {"name", "age", "email", "department"}
    updates = {key: value for key, value in data.items() if key in allowed}

    if not updates:
        return jsonify({"error": "Provide at least one valid field to update"}), 400

    if "age" in updates:
        try:
            updates["age"] = int(updates["age"])
        except (ValueError, TypeError):
            return jsonify({"error": "Age must be a valid integer"}), 400

    if student_service.get_student(student_id) is None:
        return jsonify({"error": "Student not found"}), 404

    student_service.update_student(student_id, **updates)
    return jsonify({"message": "Student updated successfully"})


@app.route("/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_service.get_student(student_id) is None:
        return jsonify({"error": "Student not found"}), 404

    student_service.delete_student(student_id)
    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
