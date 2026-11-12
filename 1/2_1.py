import numpy as np

A = np.random.randint(0, 9, size=(4, 5))
print(A)

print("Элементы 2ой строки:", A[1])
print("Cтолбец с индексом 3:", A[:,3])
print("Подмассив из строк 1-3:", A[1:4])
print("Подмассив столбцов 2-4:", A[:,2:5])