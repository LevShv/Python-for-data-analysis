import numpy as np
from scipy.sparse import coo_matrix

rng = np.random.default_rng(42)
N = 10_000
shape = (5000, 5000)

row = rng.integers(0, shape[0], size=N).tolist()
col = rng.integers(0, shape[1], size=N).tolist()
data = rng.uniform(1.0, 10.0, size=N).tolist() 

coo = coo_matrix((data, (row, col)), shape=shape)
print(f"COO nnz: {coo.nnz}")  

csr = coo.tocsr()
csr.eliminate_zeros()

print(f"CSR nnz: {csr.nnz}")

sums = {}
for r, c, v in zip(row, col, data):
    sums[(r, c)] = sums.get((r, c), 0.0) + v

expected_nnz = sum(1 for v in sums.values() if v != 0)
print(f"Ожидалось {expected_nnz}, получено {csr.nnz}")

