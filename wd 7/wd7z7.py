import numpy as np
v = np.arange(6).reshape(2,3)+1
a=np.sin(v)
c = np.arange(6).reshape(2,3)+1
b=np.cos(c)
print(np.add(a, b))