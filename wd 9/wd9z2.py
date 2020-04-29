import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
xlsx = pd.ExcelFile('D:\downloads\imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
df=df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres=df.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('Urodzenia wedlug plci')
plt.show()