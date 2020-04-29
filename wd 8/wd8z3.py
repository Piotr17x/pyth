import pandas as pd
import numpy as np
from datetime import datetime
pd.set_option('display.max_rows', None)
df=pd.read_csv('D:\downloads\zamowienia.csv',delimiter=";")
#def uni():
#    for z in df['Sprzedawca'].unique():
#        print(z)
#uni()

#def najw():
#    srt=df.sort_values(by='Utarg')
#    print(srt.tail())
#najw()

#def cnt():
#    df['Liczba zamowien']=''
#    cn=df.set_index(['Sprzedawca','Utarg','Kraj','Data zamowienia','idZamowienia']).count(level='Sprzedawca')
#    print(cn)
#cnt()

#def cntkraj():
#    df['Liczba zamowien']=''
#    cn=df.set_index(['Sprzedawca','Utarg','Kraj','Data zamowienia','idZamowienia']).count(level='Kraj')
#    print(cn)
#cntkraj()

#def cntpl(rok):
#    df['Year']=''
#    for x in range(799):
#        df['Year'][x]=df['Data zamowienia'][x][0:4]
#    df['Liczba zamowien']=''
#    ff=df.groupby('Year')
#    ff=ff.get_group(rok)
#    ff=ff.groupby('Kraj')
#    sd=ff.get_group('Polska')
#    cn=sd.set_index(['Sprzedawca','Utarg','Kraj','Data zamowienia','idZamowienia','Year']).count(level='Kraj')
#    print(cn)
#cntpl('2005')

#def cntpl(rok):
#    df['Year']=''
#    for x in range(799):
#        df['Year'][x]=df['Data zamowienia'][x][0:4]
#    ff=df.groupby('Year')
#    ff=ff.get_group(rok)
#    cn=ff.groupby('Year').agg({'Utarg':'mean'})
#    print(cn)
#cntpl('2004')

#def zapisz():
#    df['Year']=''
#    for x in range(799):
#        df['Year'][x]=df['Data zamowienia'][x][0:4]
#    ff=df.groupby('Year')
#    ff=ff.get_group('2004')
#    ff.to_csv('2004.csv',sep=';')
#    ff=df.groupby('Year')
#    ff=ff.get_group('2005')
#    ff.to_csv(r'2005.csv', sep=';')
#zapisz()