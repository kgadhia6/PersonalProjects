#Credit to https://kitchingroup.cheme.cmu.edu/blog/2013/02/21/Phase-portraits-of-a-system-of-ODEs/ for the help
#Importing
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.rcParams["mathtext.fontset"] = 'cm'

#Variables and Values
a = -.2

xlimpos = 128*2
xlimneg = -128*2
ylimpos = 128*2
ylimneg = -128*2
spacing = 16
amountsolve = 4
limdivisor = 1

tspanstart = 0
tspanend = 50
tspanamount = 2000

colourmap = mpl.colormaps['viridis']

#Stuffs
def f(Y, t):
    xt, yt = Y #Just setting up the 2 outputs, could really set this to whatever in terms of names
    return [-yt, xt + a*yt]

xt = np.linspace(xlimneg, xlimpos, spacing)
yt = np.linspace(ylimneg, ylimpos, spacing)

XT, YT = np.meshgrid(xt, yt)

t = 0

u, v = np.zeros(XT.shape), np.zeros(YT.shape)

NI, NJ = XT.shape

for i in range(NI):
    for j in range(NJ):
        x = XT[i, j]
        y = YT[i, j]
        yprime = f([x, y], t)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]

Q = plt.quiver(XT, YT, u, v, (u**2 + v**2)**(1/2), cmap=colourmap)
plt.title("2D Rössler system of equations Phase Portrait. " "$a = " + str(a) + "$")
plt.colorbar()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim([xlimneg, xlimpos])
plt.ylim([ylimneg, ylimpos])

for y20 in np.linspace(ylimpos / limdivisor, ylimneg / limdivisor, amountsolve):
    tspan = np.linspace(tspanstart, tspanend, tspanamount)
    y0 = [0.0, y20]
    ys = odeint(f, y0, tspan)
    plt.plot(ys[:,0], ys[:,1], 'b-') # path
    plt.plot([ys[0,0]], [ys[0,1]], 'o') # start
    plt.plot([ys[-1,0]], [ys[-1,1]], 's') # end
    

plt.xlim([xlimneg, xlimpos])

plt.show()

