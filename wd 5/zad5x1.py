import sys
class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        return self.rodzaj
class Ubrania(Material):
    def __init__(self,rodzaj,dlugosc,szerokosc,rozmiar,kolor,dla_kogo):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
        self.rozmiar=rozmiar
        self.dla_kogo=dla_kogo
        self.kolor=kolor
    def wyswietl_dane(self):
        return self.rozmiar,self.kolor,self.dla_kogo
class Sweter(Ubrania):
    def __init__(self,rodzaj,dlugosc,szerokosc,rozmiar,kolor,dla_kogo,rodzaj_swetra):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
        self.rozmiar=rozmiar
        self.dla_kogo=dla_kogo
        self.kolor=kolor
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self):
        return self.rozmiar,self.kolor,self.dla_kogo,self.rodzaj_swetra

sw1=Sweter("welna",30,20,"m","czarny","damski","z zamkiem")
print(sw1.wyswietl_dane())
print(sw1.wyswietl_nazwe())
ub1=Ubrania("welna",30,20,"m","czarny","damski")
print(ub1.wyswietl_dane())
print(ub1.wyswietl_nazwe())