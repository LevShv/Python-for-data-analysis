import pandas as pd

from data import data
df = pd.DataFrame(data)
df['total_comp'] = df['salary'] + df['bonus'].fillna(0)
df = df.drop('hire_date', axis=1)

count = df.isna().sum()
print("Количество пропусков в каждом столбце:\n", count)

df['salary'] = df['salary'].fillna(
    df.groupby('department')['salary'].transform('mean')
)

df['bonus'] = df['bonus'].fillna(0)

df = df.dropna(subset=['salary'])

print(df)
