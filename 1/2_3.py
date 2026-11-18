import numpy as np

A = np.random.randint(-9, 9, size=(4, 5))
print(A)
A[A < 0] = 0
print(A)