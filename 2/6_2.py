import numpy as np
size = 6
arr = np.random.randint(0, 9, size=(size, size))

print(arr)
print('подматрицу из строк 2–4 и столбцов 1–3 (включительно)')
print(arr[2:5,1:4])
print('главную диагональ через np.diagonal', arr.diagonal())
print('«шахматный» узор: элементы с чётной суммой индексов')

mask = np.zeros((6, 6), dtype=bool)
mask[::2,::2] = True
mask[1::2,1::2] = True
width = size // 2
result = np.empty((size, width), dtype=int)

for i in range(size):
   result[i] = arr[i,mask[i]]
print(result)


