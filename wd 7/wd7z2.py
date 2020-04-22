import numpy as np
b=np.arange(9).reshape(3,3)+1
a=np.arange(16).reshape(4,4)+1
print(a)
print(b,"\n")
print(b.min(axis=1))
print(b.min(axis=0))
print(a.min(axis=1))
print(a.min(axis=0))