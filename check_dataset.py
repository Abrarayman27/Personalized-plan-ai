import pandas as pd
df = pd.read_csv('wellbeing_data.csv')
print(f"Rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Plan distribution:\n{df['recommended_plan'].value_counts()}")