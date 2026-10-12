import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.prod(a)
print(c)

d = np.prod([a,b])
print(d)

e = np.prod([a,b], axis = 1)
print(e)

f = np.cumprod(a)
print(f)