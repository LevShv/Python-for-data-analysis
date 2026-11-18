import numpy as np

A = np.random.randint(0, 9, size=(10))
print(A)

def sum_squares(A):
    result = 0
    for x in A:
        result += x ** 2
    return result

print(sum_squares(A))