import sys
lista = []
with open("dane2.txt", "r+") as plik:
    for x in range(8):
        lista += ["qwerty"]
        plik.writelines(lista[x]+"\n")
    linia = plik.readline()
    for linia in plik:
        print(linia, end="")
    