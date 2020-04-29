import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
xlsx = pd.ExcelFile('D:\downloads\imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
df=df[df['Rok']+5>2017]
df=df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = df.plot.pie(subplots=True ,fontsize=20, autopct='%.2f%%', figsize=(6, 6))
plt.title('Urodzenia wedlug plci z ostatnich 5 lat')
plt.show()