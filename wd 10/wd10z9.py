import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
df=pd.read_csv('D:\downloads\zamowienia.csv',delimiter=";")
df['Liczba zamowien']=''
df=df.groupby('Sprzedawca').agg({'Liczba zamowien':'count'})
df.plot.pie(subplots=True ,shadow="true",explode=(0.5, 0.1, 0, 0,0,0,0,0,0),fontsize=20, autopct='%.2f%%', figsize=(6, 6))
plt.title("Sprzedawcy")
plt.legend().set_visible(False)
plt.show()