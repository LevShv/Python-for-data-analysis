import numpy as np

name = 'big.dat'
shape = (50000, 200)
batchSize = 100
m = np.memmap (name, dtype='float32', mode='r+', shape=shape)
mx = m[0][0]
mn = m[0][0]
sm = 0
for startIdx in range(0, shape[0], batchSize):
    endIdx = min(startIdx + batchSize, shape[0])
    batch = m[startIdx:endIdx]
    mx = max(batch.max(), mx)
    mn = min(batch.min(), mn)
    sm += batch.sum()

print("Максимальный элемент", mx)
print("Минимальный элемент", mn)
print("Среднее значение", sm/(shape[0] * shape[1]))


    




