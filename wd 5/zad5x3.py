class Kwadrat:
    def __init__(self, x):
        self.x = x
    def __ge__(self,kwadrat):
        if(self.x>=kwadrat.x):
            return "ge"
        else:
            return "lt"
    def __gt__(self,kwadrat):
        if(self.x>kwadrat.x):
            return "gt"
        else:
            return "le"
    def __le__(self,kwadrat):
        if(self.x<=kwadrat.x):
            return "le"
        else:
            return "gt"
    def __lt__(self,kwadrat):
        if(self.x<kwadrat.x):
            return "lt"
        else:
            return "ge"
kw1=Kwadrat(4)
kw2=Kwadrat(3)
print(kw1>=kw2)
print(kw1>kw2)
print(kw1<=kw2)
print(kw1<kw2)