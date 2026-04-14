import pandas as pd
import joblib
import os

from student_ai_project.dao.student_dao import save_prediction, get_all_predictions


BASE_DIR = os.path.abspath(__file__)

PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../"))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "student_regression_model.pkl")

print(MODEL_PATH)

model = joblib.load(MODEL_PATH)

def predict_marks(data):
    student = pd.DataFrame([{
        'age': data['age'],
        'study_hours': data['study_hours'],
        'attendance': data['attendance'],
        'sleep_hours': data['sleep_hours']
    }])
    marks = float(model.predict(student)[0])
    result = "PASS" if marks >= 75 else "FAIL"

    #savet to DB
    save_prediction(data, marks, result)

    return {
        "marks": round(marks,2),
        "result": result
    }
def fetch_history(limit):
    data = get_all_predictions(limit)
    return data

# Business Rules
def validate_business_rues(data):
    age = float(data['age'])
    study_hours = float(data['study_hours'])
    attendance = float(data['attendance'])
    sleep_hours = float(data['sleep_hours'])
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