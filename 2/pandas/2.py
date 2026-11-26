import numpy as np
import pandas as pd
from data import data

df = pd.DataFrame(data)

itEmployees = df.loc[df['department'] == 'IT', ['name', 'salary']]
print("Сотрудники из IT (name и salary)")
print(itEmployees)

sub = df.iloc[:3, :2]
print("Первые 3 строки и первые 2 столбца")
print(sub)

highSalary = df[df['salary'] > 70000]
print("Сотрудники с зарплатой > 70000")
print(highSalary)

df['total_comp'] = df['salary'] + df['bonus'].fillna(0)
print("Добавлен столбец total_comp")
print(df[['name', 'salary', 'bonus', 'total_comp']])

df = df.drop('hire_date', axis=1)
print("Таблица после удаления hire_date")
print(df)

df.to_pickle('data.pkl')
