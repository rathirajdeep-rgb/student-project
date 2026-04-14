def validate_request(data):
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
    return None # valid
