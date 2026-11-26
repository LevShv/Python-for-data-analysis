import timeit
import numpy as np

N = 10000000

def pythonLoop():
    res = []
    for x, y in zip(al, bl):
        res.append((x + y) / (x - y + 1))
    return res

def numpyOneline():
    return (a + b) / (a - b + 1.0)

def numpyOut():
    np.add(a, b, out=resBuf)
    np.subtract(a, b, out=tmpBuf)
    np.add(tmpBuf, 1.0, out=tmpBuf)
    np.divide(resBuf, tmpBuf, out=resBuf)
    return resBuf

a = np.memmap ('a.dat', dtype='float64', mode='w+', shape=N)
b = np.memmap ('b.dat', dtype='float64', mode='w+', shape=N)

a[:]= np.random.default_rng().random(N, dtype=np.float64)
b[:] = np.random.default_rng().random(N, dtype=np.float64)

al = a.tolist()
bl = b.tolist()

resBuf = np.empty_like(a)
tmpBuf = np.empty_like(a)

print(f"Python-цикл с list:", np.mean(timeit.repeat(pythonLoop, repeat=3, number=1)))
print(f"NumPy-выражение в одну строку:", np.mean(timeit.repeat(numpyOneline, repeat=10, number=1)))
print(f"NumPy-выражение с out= для переиспользования буфера:", np.mean(timeit.repeat(numpyOut, repeat=10, number=1)))
