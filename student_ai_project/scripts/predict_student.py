import joblib
import pandas as pd

# Load model
model = joblib.load('../models/student_model.pkl')

# New student data
new_student = pd.DataFrame(
    [{
        'age': 23,
        'study_hours': 8,
        'attendance': 30,
        'sleep_hours': 6
    }])

# predict
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)
print('Prediction (0 = Fail, 1 = Pass):', prediction[0])
print('Probability:', probability)
