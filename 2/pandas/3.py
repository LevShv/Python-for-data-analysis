import pandas as pd
df = pd.read_pickle('data.pkl')

count = df.isna().sum()
print("Количество пропусков в каждом столбце:\n", count)

df['salary'] = df['salary'].fillna(
    df.groupby('department')['salary'].transform('mean')
)

df['bonus'] = df['bonus'].fillna(0)

df = df.dropna(subset=['salary'])

print(df)

df.to_pickle('data.pkl')

