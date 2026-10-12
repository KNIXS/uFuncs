import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.diff(a)
print(c)

d = np.diff([a,b])
print(d)

e = np.diff([a,b], n = 2)
print(e)