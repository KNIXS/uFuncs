import numpy as np

def add(x,y):
    return x+y

def sub(c,d):
    return c-d

def div(e,f):
    return e/f

def multi(g,h):
    return g*h

a = np.frompyfunc(add,2,1)
print(a([1,2,3,4],[5,6,7,8]))

z = np.frompyfunc(sub,2,1)
print(z([1,2,3,4],[5,6,7,8]))

w = np.frompyfunc(div,2,1)
print(w([1,2,3,4],[5,6,7,8]))

r = np.frompyfunc(multi,2,1)
print(r([1,2,3,4],[5,6,7,8]))



