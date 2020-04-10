class Kwadrat:
    def __init__(self, x):
        self.x = x
    def __add__(self,kwadrat):
        return Kwadrat((self.x + kwadrat.x)*4)
    def __str__(self):
        return f'Kwadrat({self.x})'

k1=Kwadrat(1)
k2=Kwadrat(2)
k3=k2+k1
print(k3)