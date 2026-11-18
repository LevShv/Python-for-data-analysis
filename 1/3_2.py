import numpy as np

size = 1000
col = 5
row = 200

path = 'mass.bin'
dtype = np.dtype('float64') 
typeSize = dtype.itemsize

result = np.empty(size, dtype=dtype)

m = np.memmap(path, dtype, mode='r', shape=(size, size))
print(m[row,:])

with open(path, 'rb') as f:
    for i in range(size):
        f.seek((i * size + col) * typeSize)
        result[i] = np.frombuffer(f.read(typeSize), dtype=dtype)[0]
print(result)

