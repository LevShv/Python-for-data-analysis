import numpy as np

x = np.float32(1000000.1)
y = np.float32(1000000.0) 

print("x =", x.item())
print("y =", y.item())

if x != y:
    print("Числа отличаются на:", abs((x - y).item()))
