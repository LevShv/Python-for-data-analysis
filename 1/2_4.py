import numpy as np

B = np.random.randint(-9, 9, size=(4, 1))
C = np.random.randint(-9, 9, size=(1, 5))
print(B)
print(C)

A = B + C

print(A)