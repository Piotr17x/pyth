import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
df=pd.read_csv('D:\downloads\zamowienia.csv',delimiter=";")
df['Liczba zamowien']=''
df=df.groupby('Sprzedawca').agg({'Liczba zamowien':'count'})
print(df)
wykres=df.plot.bar()
wykres.set_ylabel('Ilosc')
wykres.set_xlabel('Nazwisko')
wykres.legend()
plt.title('Ilosc zamowien wg sprzedawcy')
plt.show()