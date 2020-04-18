import numpy as np
d=np.ones(25).astype('int64')
for n in range(2,25):
    d[n]=d[n-1]+d[n-2]
d=d.reshape(5,5)
print(d)