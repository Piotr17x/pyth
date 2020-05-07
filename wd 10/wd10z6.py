import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
xlsx = pd.ExcelFile('D:\downloads\imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
d1=df.groupby(['Plec']).agg({'Liczba':['sum']})
d2m=df[df['Plec']=='M']
d2m=d2m.groupby(['Rok']).agg({'Liczba':['sum']})
d2k=df[df['Plec']=='K']
d2k=d2k.groupby(['Rok']).agg({'Liczba':['sum']})
d3=df.groupby(['Rok']).agg({'Liczba':['sum']})
fig, axes = plt.subplots(nrows=1, ncols=3)
d1.plot(ax=axes[0],kind='bar')
d2m.plot(ax=axes[1])
d2k.plot(ax=axes[1])
d3.plot(ax=axes[2],kind='bar')
plt.show()