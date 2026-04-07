from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('models/student_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        sleep_hours = float(request.form['sleep_hours'])
        student = pd.DataFrame([{'age': age,
                            'study_hours': study_hours,
                            'attendance': attendance,
                            'sleep_hours': sleep_hours}])

        marks = model.predict(student)[0]
        result = 'Pass' if marks >=75 else 'Fail'
        return render_template(
            'index.html', prediction_text = f"Marks: {marks:.2f} | Result: {result}")

    except Exception as e:
        return render_template('index.html', prediction_text = f"Error: {str(e)}")
if __name__ == '__main__':
    app.run(debug=True)