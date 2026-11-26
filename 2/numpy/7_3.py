import timeit
import numpy as np

shape = (3000, 3000)

def init(m):
    m[:,:] = np.random.default_rng().random(shape, dtype=np.float32)

def rowSum(m):
    sum = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            sum += m[i,j]
    return sum

def colSum(m):
    sum = 0
    for i in range(shape[1]):
        for j in range(shape[0]):
            sum += m[j,i]
    return sum

co = np.memmap ('co.dat', dtype='float32', mode='w+', shape=shape)
fo = np.memmap ('fo.dat', dtype='float32', mode='w+', shape=shape, order='F')

init(co)
init(fo)

times = timeit.repeat(lambda: rowSum(co), repeat=10, number=1)
print("Время прогона массива c-order по строчно", np.mean(times))

times = timeit.repeat(lambda: colSum(co), repeat=10, number=1)
print("Время прогона массива c-order по столбцам", np.mean(times))

times = timeit.repeat(lambda: rowSum(fo), repeat=10, number=1)
print("Время прогона массива f-order по строчно", np.mean(times))

times = timeit.repeat(lambda: colSum(fo), repeat=10, number=1)
print("Время прогона массива f-order по столбцам", np.mean(times))