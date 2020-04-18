import numpy as np
def gen(n):
    c=np.ones((n,n))
    c=c.astype('int64')+1
    for x in range(n):
        for y in range(n):
            c[x,y]=c[x,y]+abs(x-y)*2
    return c
print(gen(3))
