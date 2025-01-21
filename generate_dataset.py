import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'Machine_ID': np.arange(1, 101),
    'Temperature': np.random.randint(60, 100, 100),
    'Run_Time': np.random.randint(50, 200, 100),
    'Downtime_Flag': np.random.choice([0, 1], 100, p=[0.8, 0.2])
}

df = pd.DataFrame(data)
df.to_csv('uploads/manufacturing_data.csv', index=False)
print("Dataset created and saved as 'uploads/manufacturing_data.csv'")
