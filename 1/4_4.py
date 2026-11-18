import numpy as np
import time
from scipy.sparse import random as sparse_random

def time_measure(A, B, count):
    start = time.perf_counter()
    for i in range(count):
        C = A @ B
    end = time.perf_counter()
    return end - start

size = 1000
Ac = sparse_random(size, size, density=0.01, format='csr', random_state=10)
Bc = sparse_random(size, size, density=0.01, format='csr', random_state=10)

A = Ac.toarray()
B = Bc.toarray()

count = 30

print("Умножение разряженных:", time_measure(Ac, Bc, count))
print("Умножение плотных:", time_measure(A, B, count))


