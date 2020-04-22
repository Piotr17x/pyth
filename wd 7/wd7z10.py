import numpy as np
a=np.arange(81).reshape(9,9)+1
print(a,"\n")
print(a.ravel(),"\n")
print(a.reshape(81,1),"\n")
#macierz 9x9 możemy tylko spłaszczyc 
#w poziomie lub pionie
#takiej liczby (81) nie można umiescic 
#w macierzy inaczej