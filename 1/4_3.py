import numpy as np
from scipy.sparse import random as sparse_random

size = 5
A = sparse_random(size, size, density=0.2, format='csr', random_state=10)
print(A)

vector = np.random.randint(1, 10, size=size)
print(vector)

print(A @ vector)