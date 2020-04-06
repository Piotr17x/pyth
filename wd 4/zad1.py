import sys
x=range(101)
plik = open("dane.txt","w+")
for n in x:
    if n%4==0:
        plik.write(str(n))