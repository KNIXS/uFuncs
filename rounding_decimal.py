import numpy as np

a = np.trunc([1.001,2.90,3.897,4.6476])
print(a)

b = np.fix([1.001,2.90,3.897,4.6476])
print(b)

c = np.around(3.167777,1)
print(c)

d = np.floor([3.167777,2.8999])
print(d)

e = np.ceil([3.167777,2.8999])
print(e)