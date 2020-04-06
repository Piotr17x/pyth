import sys
class NaZakupy:
    nazwa_produktu=""
    ilosc=""
    jednostka_miary=""
    cena_jed=""
    def __init__(self, nazwa_produktu, ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyświetl_produkt(self):
        return "Nazwa",self.nazwa_produktu,"jednostka miary",self.jednostka_miary,"cena_jed",self.cena_jed
    def ile_produktu(self):
        return "Ilość",self.ilosc,"jednostka miary",self.jednostka_miary
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed,"zl"
produkt=NaZakupy("pomidor",2,"1 kg",5)
print(produkt.ile_kosztuje())
