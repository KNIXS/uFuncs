import math
import numpy as np
from math import log

a = np.arange(1,10,2)
print(np.log2(a))

b = np.arange(1,10,2)
print(np.log10(b))

c = np.arange(1,10,2)
print(np.log(c))

d = np.frompyfunc(log,2,1)
print(d(100,15))