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
def fetch_history():
    data = get_all_predictions()
    return data
