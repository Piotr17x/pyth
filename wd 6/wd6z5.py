import numpy as np
def dia(x):
    b=np.arange(1,x+1,1)
    b=np.flip(b)
    b=np.diag(b)
    return b
print(dia(4))