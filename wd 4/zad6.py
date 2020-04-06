import sys
class slowa:
    slowo1=""
    slowo2=""
    def __init__(self, slowo1, slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def sprawdz_czy_palindrom(self):
        if self.slowo1==self.slowo1[::-1]:
            return "jest to palindrom"
        else:
            return "to nie jest palindrom"
    def sprawdz_czy_metagramy(self):
        k=len(self.slowo1)
        for n in range(len(self.slowo1)):
            if self.slowo1[n]==self.slowo2[n]:
                k-=1
        if k==1:
            return "sa to metagramy"
        else:
            return "to nie sa metagramy"
    def sprawdz_czy_anagram(self):
        for n in range(len(self.slowo1)):
            if self.slowo1.count(self.slowo1[n])!=self.slowo2.count(self.slowo1[n]):
                return"to nie sa anagramy"
        return "to sa anagramy"
    def wyswietl_wyrazy(self):
        return self.slowo1,self.slowo2
gry=slowa("kajak","kajak")
print(gry.wyswietl_wyrazy())