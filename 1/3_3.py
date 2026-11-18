import numpy as np
import time

def row_major(m, nrows, ncols):
    sm = 0
    for i in range(nrows):
        for j in range(ncols):
            sm += m[i,j]
    return sm

def column_major(m, nrows, ncols):
    sm = 0
    for j in range(ncols):
        for i in range(nrows):
            sm += m[i,j]
    return sm

def time_measure(func, m, nrows, ncols, count):
    start = time.perf_counter()
    for i in range(count):
        func(m, nrows, ncols)
    end = time.perf_counter()
    return end - start

size = 1000
count = 30
m = np.memmap('mass.bin', 'float64', mode='r', shape=(size, size))

print(f'row_major: {time_measure(row_major, m, size, size, count)}')
print(f'column_major: {time_measure(column_major, m, size, size, count)}')

