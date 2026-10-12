import numpy as np

a = np.array([1,2,4,5,2,8,5,6])
b = np.array([3,2,2,3,4,7,9,6])
d = [np.unique(a)]
print(d)

e = np.union1d(a,b)
print(e)

f = np.intersect1d(a,b)
print(f)

g = np.setdiff1d(a,b)
print(g)

h = np.setxor1d(a,b)
print(h)