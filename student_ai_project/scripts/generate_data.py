import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'age': np.random.randint(18,30, 50),
    'study_hours': np.random.randint(1,9, 50),
    'attendance': np.random.randint(50,100, 50),
    'sleep_hours': np.random.randint(5,9, 50),
}

df = pd.DataFrame(data)
df['marks'] =  (df['study_hours']*9
                + df['attendance'] *0.2
                + df['sleep_hours']*2
                +np.random.randint(-5, 5, 50)).astype(int)
df.to_csv('student_data.csv', index=False)
print('Dataset created')
