import numpy as np
import os

name = 'big.dat'
shape = (50000, 200)
m = np.memmap (name, dtype='float32', mode='w+', shape=shape)
m[:,:] = np.random.default_rng().random(shape, dtype=np.float32)

actual_size = os.path.getsize(name)
expected_size = 50000 * 200 * 4

print("Текущий размер файла =", actual_size, "Ожидаемый =", expected_size)