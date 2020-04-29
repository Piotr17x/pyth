import pandas as pd
import numpy as np
import xlrd
import openpyxl
pd.set_option('display.max_rows', None)
xlsx = pd.ExcelFile('D:\downloads\imiona.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
#def sa(year):
#    print(df[((df.Rok==year)&(df.Liczba>1000))])
#sa(2000)

#def ab(im):
#    print(df[(df.Imie==im.upper())])
#ab('Piotr')

#def ac(p,k):
#    suma=0
#    grouped = df.groupby(['Rok'])
#    for i in range(k+1-p):
#        c=grouped.get_group(i+p)
#        suma+=c.agg({'Liczba':['sum']})
#    print(suma)
#ac(2000,2017)

#def ac(p,k):
#    suma=0
#    grouped = df.groupby(['Rok'])
#    for i in range(k+1-p):
#        c=grouped.get_group(i+p)
#        suma+=c.agg({'Liczba':['sum']})
#    print(suma)
#ac(2000,2005)

#def plec():
#    grouped=df.groupby(['Plec'])
#    m=grouped.get_group('M')
#    sumach=m.agg({'Liczba':['sum']})
#    k=grouped.get_group('K')
#    sumadz=k.agg({'Liczba':['sum']})
#    print("chlopcy ",sumach['Liczba'],"\ndziewczynki",sumadz['Liczba'])
#plec()

#def poprok(year):
#    groupy= df.groupby(['Rok'])
#    y=groupy.get_group(year)
#    groupp=y.groupby(['Plec'])
#    d=groupp.get_group('K')
#    c=groupp.get_group('M')
#    print(c.iloc[[0],[1]],'\n',d.iloc[[0],[1]])
#poprok(2002)

#def popokr(p,k):
#    okres=df[((df.Rok>=p)&(df.Rok>=k))]
#    plec=okres.groupby('Plec')
#    c=plec.get_group('M')
#    d=plec.get_group('K')
#    grpc=c.groupby(['Imie']).agg({'Liczba':'sum'})
#    grpd=d.groupby(['Imie']).agg({'Liczba':'sum'})
#    grpcs=grpc.sort_values(by='Liczba')
#    grpds=grpd.sort_values(by='Liczba')
#    print(grpcs.iloc[[-1],[0]])
#    print(grpds.iloc[[-1],[0]])
#popokr(2001,2001)