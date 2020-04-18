import numpy as np
def f1 (n):
    m =np.arange((n*n))
    m=m.reshape(n,n)
    m=m+1
    return m
print(f1(3))