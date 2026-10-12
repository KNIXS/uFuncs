import numpy as np

a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
c = []
for i, j in zip(a, b):
    c.append(i + j)
print(c)

d = np.add(a,b)
print(d)