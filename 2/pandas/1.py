import numpy as np
import pandas as pd
from data import data

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)

df = pd.DataFrame(data)

print("Первая строка:")
print(df.head(1))

print("Последняя строка:")
print(df.tail(1))

print("Информация о типах данных:")
df.info()

print("Статистика:")
print(df.describe())
