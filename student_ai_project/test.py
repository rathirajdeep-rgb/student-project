import requests

data= {
    'age': 20,
    'study_hours': 6,
    'attendance': 90,
    'sleep_hours': 19
}

res = requests.post('http://127.0.0.1:5000/predict', json=data)
print(res.json())