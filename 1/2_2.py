import numpy as np

A = np.random.randint(0, 9, size=(4, 5))
print(A)
print(A[[0, 2, 3]][:,[1, 4]])