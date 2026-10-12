import numpy as np

a = np.sin(np.pi/2)
print(a)

b = np.sin([np.pi/2,np.pi/3,np.pi/4])
print(b)

c = np.array([10,20,30,40])
d = np.deg2rad(c)
e = np.rad2deg(c)
f = np.arcsin(c)
print(d)
print(e)
print(c)

base = 4
prep = 3

hypo = np.hypot(base,prep)
print(hypo)