import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def rzucaj(x):
    kostka1=np.random.randint(1,7,x)
    kostka2=np.random.randint(1,7,x)
    return kostka1+kostka2

plt.hist(rzucaj(10), bins=10, facecolor='g', alpha=0.75, density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid(True)
plt.show()