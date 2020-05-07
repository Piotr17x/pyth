import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
df=pd.read_csv('D:\downloads\iris.csv',delimiter=",",header=None)
plt.scatter(df[1],df[0],c=np.random.randint(0, 50, 150),s=np.abs(df[1]-df[0]))
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.annotate("losowe kolory",xy=(3,7),
arrowprops=dict(facecolor='black', shrink=0.03),xytext=(2, 7.5))
plt.show()
