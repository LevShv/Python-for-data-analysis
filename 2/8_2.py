import timeit
import numpy as np
from scipy.sparse import random as sparse_random

shape = (4000, 4000)
density = 0.005
rng = np.random.default_rng(42)

csr = sparse_random(shape[0], shape[1], density=density, format='csr', dtype=np.float64, random_state=rng)
dense = csr.toarray()
vec = rng.random(shape, dtype=np.float64)

denseBytes = dense.nbytes
csrBytes = csr.data.nbytes + csr.indices.nbytes + csr.indptr.nbytes

print(f"Обьем памяти dense: {denseBytes} байт")
print(f"Обьем памяти CSR: {csrBytes} байт")

tdense = np.mean(timeit.repeat(lambda: dense @ vec, repeat=5))
tcsr = np.mean(timeit.repeat(lambda: csr @ vec, repeat=5))

print(f"Время умножения dense на vec: {tdense}")
print(f"Время умножения CSR на vec): {tcsr}")
