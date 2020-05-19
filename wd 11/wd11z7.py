import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()

ax = fig.gca( projection = '3d' )

t2 = np.linspace( 0 , 2 * np.pi, 5 )
z=t2
x = np.sin(t2)
y = np.sin(t2)
ax.plot(x, y, z, label = 'waz',c='g' )



n = 20
for zlow, zhigh in [( 0, 6 )]:
    x = randrange(n, -2 , 2 )
    y = randrange(n, -1 , 1 )
    z = randrange(n, zlow, zhigh)
    ax.scatter(x, y,z,zdir='none', c ='r', marker ='o',label='jablka')
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

ax.legend()
ax.view_init( elev = 20 , azim = -25 )
plt.show()