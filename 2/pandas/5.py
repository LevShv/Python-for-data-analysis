import pandas as pd

df = pd.read_pickle('data.pkl')

depts = df['department'].dropna().unique()
managers = pd.DataFrame({
    'department': depts,
    'manager': [f'Руководитель_{i+1}' for i in range(len(depts))]
})

df = pd.merge(df, managers, on='department', how='left')
manager = managers.loc[managers['department'] == 'IT', 'manager'].iloc[0]

newEmployee = pd.DataFrame([{
    'name': 'John',
    'department': 'IT',
    'salary': 120000,
    'bonus': 15000,
    'manager': manager
}])

df = pd.concat([df, newEmployee])
df = df.reset_index(drop=True)

print(df)

df.to_pickle('data.pkl')
