from Tools.demo.sortvisu import steps
from flask import Blueprint, request, jsonify
from student_ai_project.services.student_service import predict_marks, fetch_history

student_bp = Blueprint('student_bp', __name__)


def validate_input(data):
    required_attributes = ['age', 'study_hours', 'attendance', 'sleep_hours']
    #check missing attributes
    for attribute in required_attributes:
        if attribute not in data:
            return f"{attribute} is required"
    # check data types
    try:
        age = float(data['age'])
        study_hours = float(data['study_hours'])
        attendance = float(data['attendance'])
        sleep_hours = float(data['sleep_hours'])
    except:
        return  "All attributes must be numbers"

    # Business Rules
    if age < 18:
        return "Age must be >= 18 years"
    if not (0<= study_hours <= 24):
        return "Study hours must be between 0 ans 24"
    if not (0<=attendance<=100):
        return "Attendance must be between 0 and 100"
    if not (0<= sleep_hours <= 24):
        return "Sleep hours must be between 0 and 24"
    if sleep_hours + study_hours > 24:
        return "sum of Sleep hours and Study hours cannot be more than 24"
    return None # valid

@student_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # validation steps
        error = validate_input(data)
        if error:
            return jsonify({'error': error}), 400
        result = predict_marks(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_bp.route('/history', methods=['GET'])
def get_history():
    try:
                return jsonify(fetch_history())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


