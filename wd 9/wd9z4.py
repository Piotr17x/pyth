import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
df=pd.read_csv('D:\downloads\iris.csv',delimiter=",",header=None)

groups = df.groupby(4)
for name, group in groups:
    plt.plot(group[1], group[0], marker="o", linestyle="", label=name)
plt.legend()
plt.show()