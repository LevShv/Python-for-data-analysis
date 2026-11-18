from sum_squares import sum_squares_c
import numpy as np
import time

def sum_squares(A):
    result = 0
    for x in A:
        result += x ** 2
    return result

def time_measure(func, A, count):
    start = time.perf_counter()
    for i in range(count):
        res = func(A)
    end = time.perf_counter()
    return end - start

A = np.random.randint(0, 9, size=(10000000)).tolist()
count = 10

print("Python:", time_measure(sum_squares, A, count))
print("CPython:", time_measure(sum_squares_c, A, count))