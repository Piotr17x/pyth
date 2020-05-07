import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
xlsx = pd.ExcelFile('D:\downloads\imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
d2m=df[df['Plec']=='M']
d2m=d2m.groupby(['Rok']).agg({'Liczba':['sum']})
d2k=df[df['Plec']=='K']
d2k=d2k.groupby(['Rok']).agg({'Liczba':['sum']})
d3=df.groupby(['Rok']).agg({'Liczba':['sum']})
d3.columns = ['Liczba']
d2m.columns = ['Liczba']
d2k.columns = ['Liczba']
width=0.3
rok=np.arange(2000,2018,1)
plt.xticks(rok,rotation=45)
plt.bar(rok,d2m['Liczba'],width,color="blue",label="M")
plt.bar(rok,d2k['Liczba'],width,color="red",label="K",bottom=d2m['Liczba'])
plt.legend()
plt.show()