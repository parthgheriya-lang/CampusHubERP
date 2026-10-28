from flask import Blueprint, jsonify, request
from app.services.faculty_service import FacultyService
from app.models.faculty import Faculty

faculty_api = Blueprint("faculty_api", __name__)
faculty_service = FacultyService()


@faculty_api.route("/faculty", methods=["GET"])
def get_all_faculty():
    return jsonify([
        faculty.to_dict()
        for faculty in faculty_service.get_all_faculty()
    ])


@faculty_api.route("/faculty/<faculty_id>", methods=["GET"])
def get_faculty(faculty_id):
    faculty = faculty_service.get_faculty(faculty_id)

    if faculty is None:
        return jsonify({"error": "Faculty not found"}), 404

    return jsonify(faculty.to_dict())


@faculty_api.route("/faculty", methods=["POST"])
def create_faculty():
    data = request.get_json(silent=True) or {}

    required = ["faculty_id", "name", "age", "email", "department"]
    if any(field not in data for field in required):
        return jsonify({"error": "All faculty fields are required"}), 400

    try:
        faculty = Faculty(
            data["faculty_id"],
            data["name"],
            int(data["age"]),
            data["email"],
            data["department"]
        )
        faculty_service.create_faculty(faculty)

        return jsonify({
            "message": "Faculty created successfully",
            "faculty_id": faculty.faculty_id
        }), 201
    except (ValueError, TypeError) as error:
        return jsonify({"error": str(error)}), 400


@faculty_api.route("/faculty/<faculty_id>", methods=["PUT"])
def update_faculty(faculty_id):
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

    if faculty_service.get_faculty(faculty_id) is None:
        return jsonify({"error": "Faculty not found"}), 404

    try:
        faculty_service.update_faculty(faculty_id, **updates)
        return jsonify({"message": "Faculty updated successfully"})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@faculty_api.route("/faculty/<faculty_id>", methods=["DELETE"])
def delete_faculty(faculty_id):
    if faculty_service.get_faculty(faculty_id) is None:
        return jsonify({"error": "Faculty not found"}), 404

    faculty_service.delete_faculty(faculty_id)
    return jsonify({"message": "Faculty deleted successfully"})
