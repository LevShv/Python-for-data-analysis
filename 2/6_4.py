import numpy as np

x = np.random.randn(1000)

print("подсчитайте количество элементов, больших 1: ", (x > 1).sum())

tx = np.where(x < 0, 0, x)
print("амените все отрицательные элементы на 0", tx )
print("проверка на наличие отрицательных элементов", (tx < 0).sum())

print("обнулите элементы, стоящие на позициях, где соседи (слева и справа) имеют разные знаки(т.е. где происходит смена знака)")

print(x,"\n")
mask = np.ones(1000, dtype=bool)
for i in range(1, len(x) - 1):
    if x[i - 1] * x[i + 1] < 0:
        mask[i] = False
x[~mask] = 0 

print(x)