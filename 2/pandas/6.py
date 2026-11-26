import pandas as pd

df = pd.read_pickle('data.pkl')
df['total_comp'] = df['salary'] + df['bonus']


top = df.nlargest(3, 'total_comp')
print("Топ-3 сотрудников по общей компенсации:\n", top, "\n")

deptMeans = df.groupby('department')[['salary', 'bonus']].mean().reset_index()
print("Средняя зарплата и средний бонус по отделам:\n", deptMeans, "\n")

highSalaryShare = (
    df.assign(above_75k=df['salary'] > 75000)
    .groupby('department')['above_75k']
    .mean()
    .reset_index(name='share_above_75k')
)

print("Доля сотрудников с зарплатой выше 75000 по отделам:\n", highSalaryShare)
df.to_pickle('data.pkl')