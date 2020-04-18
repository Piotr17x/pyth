import numpy as np
def generuj(x,y):
    b=np.logspace(1,y, num=y,base=x )
    b=b.astype('int64')
    return b
print(generuj(3,4))