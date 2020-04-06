import sys
class Robaczek:
    x=0
    y=0
    krok=0
    ile_krokow=0
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        self.y+=ile_krokow*self.krok
    def idz_w_dol(self,ile_krokow):
        self.y-=ile_krokow*self.krok
    def idz_w_lewo(self,ile_krokow):
        self.x-=ile_krokow*self.krok
    def idz_w_prawo(self,ile_krokow):
        self.x+=ile_krokow*self.krok
    def pokaz_gdzie_jestes(self):
        return "x,y=",self.x,self.y
ruch=Robaczek(1,1,2)
ruch.idz_w_gore(1)
ruch.idz_w_dol(2)
ruch.idz_w_prawo(3)
ruch.idz_w_lewo(1)
print(ruch.pokaz_gdzie_jestes())
