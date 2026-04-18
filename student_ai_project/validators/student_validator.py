from student_ai_project.utils.exceptions import ValidationError

def validate_request(data):
    if not data:
        raise ValidationError("Request body is missing")
    required_attributes = ['age', 'study_hours', 'attendance', 'sleep_hours']
    #check missing attributes
    for attribute in required_attributes:
        if attribute not in data:
            raise ValidationError(f"{attribute} is required")
    # check data types
    try:
        age = float(data['age'])
    except ValueError:
        raise ValidationError("Age must be a number")
    try:
        study_hours = float(data['study_hours'])
    except ValueError:
        raise ValidationError("Study_hours must be a number")
    try:
        attendance = float(data['attendance'])
    except ValueError:
        raise ValidationError("Attendance must be a number")
    try:
        sleep_hours = float(data['sleep_hours'])
    except ValueError:
        raise ValidationError("Sleep hours must be a numbers")
