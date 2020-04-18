import numpy as np
def half(a,kierunek):
    x2=a.shape[0]
    y2=a.shape[1]
    if(kierunek=='x'):
        if(x2%2==1):
            return 'nieprawidlowy rozmiar macierzy'
        else:
            return a[:int(x2/2)]
    if(kierunek=='y'):
        if(y2%2==1):
            return 'nieprawidlowy rozmiar macierzy'
        else:
            return a[:,:int(y2/2)]
    
d = np.arange(36)+1
d = d.reshape((6,6))

print(half(d,'y'))




