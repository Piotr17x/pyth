import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure( figsize =plt.figaspect( 0.5 ))

ax = fig.add_subplot( 121 , projection = '3d' )
n = 20
for zlow, zhigh in [( - 50 , - 25 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c ='y', marker ='o')
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
ax.set_title('20 pkt')

ax2 = fig.add_subplot( 122 , projection = '3d' )
t2 = np.linspace( 0 , 2 * np.pi, 5 )
z2 = t2
x2 = np.sin(t2)*np.cos(t2)
y2 = np.tan(t2)
ax2.plot(x2, y2, z2, label = 'liniowy' )
ax2.set_title('5 pkt')
ax2.legend()


plt.show()