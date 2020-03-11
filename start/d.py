print("SSSSS")

# for element in kolekcja:
#     for element in kolekcja2:

def funkcja():
    print("Ala")
    a = 5
    imie = "Zbyszek"

a = 5
print(type(a))

imie = "Ala"
imie = 'Ala'
imie = """Ala
ma kota"""
print(imie)
imie = 6
imie = 6.4
print(type(imie))

liczba = int("6")
print(type(liczba))

imie = "ala"
imie=imie.capitalize()
print(imie)
print(imie[0])

print("ala".capitalize().count("A"))

print(imie+imie)

# formatowanie wyjscia

print(imie+" ma "+ str(5)+ " lat ")
print("{} ma {} lat".format(imie, 5))
print("{1} ma {0} lat".format(imie, 5))
wiek = 5
print(f"{imie} ma {wiek} lat")

# listy


lista=[]
lista=[1,4,"Ala",4.5,imie,[1,2]]
lista[0]
lista[5][1]  # 2
lista.append(3)
lista[0]=10
lista2=lista+lista
lista_nowa=list()

# slownik(tablica hash)

slownik = {}
slownik = {"imie":"Marek",
"wiek":5}
slownik["imie"]
print(slownik.keys())
print(slownik.values())
print(slownik.items())

def pow():
    pass

from math import *
import math as m



