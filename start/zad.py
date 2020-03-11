#import this
imie='Marianna'
lista=[]
for litera in imie:
    lista.append(litera.upper())

#print(lista)
#print([litera.upper() for litera in imie])
#[print(litera.upper()) for litera in imie]

# suma cyfr
#liczba=123456789
#print(sum([int(cyfra) for cyfra in str(liczba)]))

#  lista=[[1,2],[3,4]]
#print([element for wiersz in lista for element in wiersz if element %2==0])

#for wiersz in lista:
#    for element in wiersz:
#        if element % 2==0
#            wynik.append(element)

imie='Marianna'
# range(len(imie))

# slownik={klucz:wartosc for klucz,wartosc in enumerate(imie)}
# print(slownik[0])
# print(slownik)
# slow_odwr={wartosc:klucz for klucz,wartosc in slownik.items()}
# print(slow_odwr)

# set/zbiory
litery=set(imie)
# print(litery)


# rozpakowanie krotki
imie,nazwisko=('Adam','Dam')

# print(set(range(9)))
# print({*range(9)})

# funkcje

# def dodaj(liczba1,liczba2):
    # return liczba1+liczba2

# print(dodaj(2,3))
# def witaj(imie='Jan'):
    # print(f'witaj {imie}')

# witaj()
# witaj('Arkadiusz')

# moduly i pakiety

# import d

# sl={'sss':'Max x'}
# print(sl['sss'])

# slice


# print(imie[-1]) # ostatni
# print(imie[-2:]) # 2 ostatnie
# print(imie[:]) # wszystko
# print(imie[::-2])

# zad 4 (funkcje matematyczne)

# from math import *
# print(e**10) # do potegi 10
# print(pow(e,10)) #e do potegi 10
# print(pow(log(5),1/2)) #pierwiastek 2 stopnia z ln(5)
# zad6 cw1

# zdanie='ls ls ls'
# print(zdanie.count('ls'))

#zad 12

# zdanie='AB CD EF GH IJ'
# lista=zdanie.split()
# print(lista)

# zad16 (zliczenie liczby elementów)

# gry={1:'a',2:'b'}
# print(len(gry))