import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100
for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 ), ( 'b' , '^' , - 30 , - 5 ),( 'y' , 's' , - 50 , - 25 ),( 'black' , 'p' , - 50 , - 25 ),( 'g' , 'v' , - 50 , - 25 )]:
    xs = randrange(n, 21 , 35 )
    zs = randrange(n, 23 , 42 )
    cs = randrange(n, 13 , 32 )
    ys = randrange(n, 0 , 100 )
    bs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs,bs,cs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()