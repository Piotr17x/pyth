import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 30, 0.1)
s = np.sin(x)+2
c = np.sin(x)*-1
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x), sin(x)")
plt.legend(loc='center left')
plt.show()
