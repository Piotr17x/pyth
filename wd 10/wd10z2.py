import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1, 20, 20)
plt.plot(x,1/x,'g:>',label="f(x)=1/x")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([1, 20, 0, 1])
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.legend()
plt.show()