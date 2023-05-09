import numpy as np #Numerical computational library
import matplotlib.pyplot as plt #Graphical plotting library
import matplotlib as mpl

#Domain tuples (lower, upper, amount)
xd = (-20, 20, 7) #Do not confuse with dx
yd = (-20, 20, 7) #Do not confuse with dy
zd = (0, 40, 5) #Do not confuse with dz

#Differential system parameters
a = .1
b = .1
c = 14

#Graphical parameters
linelength = 2.5
elev = 10
azim = -60
colormap = plt.cm.get_cmap("viridis")
numlevels = 100
plt.rcParams["mathtext.fontset"] = 'stix'
name = "Rössler\ Attractor" #Use matplotlib mathtext
var1 = r'a' #Use mathtext for these and other variables
var2 = r'b'
var3 = r'c'
title = ((r'$\mathrm{%s\ Phase\ Space}$' % (name)) + "\n" +  '$%s = %.1f,\/ %s = %.1f,\/ %s = %.1f$' % (var1, a, var2, b, var3, c))

def diffeq(x: float, y: float, z: float) -> np.ndarray:
    dx = -y - z
    dy = x + a*y
    dz = b + z*(x - c)
    return np.array([dx, dy, dz])

x, y, z = np.meshgrid(np.linspace(*xd), np.linspace(*yd), np.linspace(*zd)) #Unpacking our domain tuples into linspace
u, v, w = diffeq(x, y, z)

ax = plt.figure().add_subplot(111, projection='3d')
ax.view_init(elev=elev, azim=azim)
mag = np.sqrt(u**2 + v**2 + w**2)
norm = mpl.colors.Normalize(vmin = mag.min(), vmax = mag.max() + .01)
mappable = mpl.cm.ScalarMappable(norm, colormap)
for i, val in np.ndenumerate(mag):
    ax.quiver(x[i], y[i], z[i], u[i], v[i], w[i], color=mappable.to_rgba(val), length = linelength, normalize=True)
    continue
ax.set_xlabel(r'$X\mathrm{\ axis}$')
ax.set_ylabel(r'$Y\mathrm{\ axis}$')
ax.set_zlabel(r'$Z\mathrm{\ axis}$')
ax.set_title(title)
cbar = plt.colorbar(mappable, location='left')
cbar.set_label(r'$\mathrm{Vector\ Magnitude}$')
plt.show()
