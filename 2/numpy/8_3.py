import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import random as sparse_random

n = 2000
densities = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
rng = np.random.default_rng(42)

x = rng.random(n, dtype=np.float64)

dense_times = []
csr_times = []
point = None


for d in densities:
    csr = sparse_random(n, n, density=d, format='csr', dtype=np.float64, random_state=rng)
    dense = csr.toarray()
    
    tdense = (np.mean(timeit.repeat(lambda: dense @ x, repeat=10, number=20)) / 20) * 1000
    tcsr = (np.mean(timeit.repeat(lambda: csr @ x, repeat=10, number=20)) / 20) * 1000
    
    dense_times.append(tdense)
    csr_times.append(tcsr)

    if point is None and tcsr >= tdense:
        point = d

print(f"Точка, где sparse перестаёт выигрывать density = {point}")


plt.figure(figsize=(9, 5))
plt.plot(densities, dense_times, marker='o', label='Dense')
plt.plot(densities, csr_times, marker='s', label='Sparse')

plt.xscale('log')  
plt.xlabel('Плотность матрицы density')
plt.ylabel('Время умножения A @ x')
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
