import numpy as np
from scipy.sparse import random as sparse_random

A = sparse_random(5, 5, density=0.2, format='csr', random_state=10)
cooA = A.tocoo()
cscA = A.tocsc()

print('CSR:')
print(A)
print('COO:')
print(cooA)
print('COO:')
print(cscA)