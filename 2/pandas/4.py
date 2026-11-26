import pandas as pd

df = pd.read_pickle('data.pkl')

msalary = df.groupby('department')['salary'].mean()
print("4.1 Средняя зарплата по отделам:\n", msalary, "\n")

stats = df.groupby('department').agg(
    msalary=('salary', 'mean'),
    maxBonus=('bonus', 'max'),
    count=('salary', 'count')
)
print("Статистика по отделам:\n", stats, "\n")

pivot_salary = df.pivot_table(
    index='department',
    values='salary',
    aggfunc='mean'
)
print("Сводная таблица:\n", pivot_salary, "\n")

sorted_depts = msalary.sort_values(ascending=False)

