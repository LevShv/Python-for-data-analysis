import numpy as np

m = np.array([0.1, 0.2, 0.3], dtype = np.float32)

exact = 0.6
result = m.sum().item()

print("Точное значение:", exact)
print("Результат сложения:", result)
print("Разница:", result - exact)

