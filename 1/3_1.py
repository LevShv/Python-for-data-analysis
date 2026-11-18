import numpy as np

m = np.memmap('mass.txt', dtype='float64', mode='w+', shape=(1000, 1000))
m[:,:] = np.random.randint(-9, 9, size=(1000, 1000))
