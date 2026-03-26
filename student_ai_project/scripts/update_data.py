import pandas as pd
import numpy as np
import os

#load existing data
file_path = os.path.join(os.path.dirname(__file__), '../data/student_data.csv')

df = pd.read_csv(file_path)
print('Original data Preview')
print(df.head())

# add noise
noise = np.random.normal(0,10,len(df))

df['marks'] = df['marks'] + noise

#convert to integer
df['marks'] = (df['marks']).astype(int)

# keep marks in valid range
df['marks'] = df['marks'].clip(0, 100)

#save updated file
df.to_csv(file_path, index=False)

print('\n Updated Data Preview \n')
print(df.head())
print(df.tail())


