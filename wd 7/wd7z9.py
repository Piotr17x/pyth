import numpy as np
a=np.arange(9).reshape(3,3)+1
for b in a.flat:
    print(b)