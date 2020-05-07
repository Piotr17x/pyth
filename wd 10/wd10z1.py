import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1, 20, 20)
plt.plot(x,1/x,label="f(x)=1/x")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([1, 20, 0, 1])
plt.legend()
plt.annotate("wykres maleje",xy=(5,0.2),
arrowprops=dict(facecolor='black', shrink=0.03),xytext=(7.5, 0.5))
plt.show()