import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["mathtext.fontset"] = 'stix'

#Parameters
xyz0 = (0., 1., 0.) #Initial value tuple (x0, y0, z0)
a = 0.1
b = 0.1
c = 14

#Graph settings (Mostly title)
elev = 30
azim = -60
name = "Rössler\ Attractor" #Add the \[space] for any spaces
var1 = 'a' #System variable names; use matplotlib mathtext for these
var2 = 'b' #e.g \alpha for alpha
var3 = 'c' #Fractions can also be used
title = ((r'$\mathrm{%s\ via\ Euler\ method}$' % (name)) + "\n" +  r'$a = %.1f,\/ b = %.1f,\/ c = %.1f $' % (a, b, c))

#Differential equation
def diffeq(xyz: "Coordinate tuple; point of interest") -> "Gradient at (x,y,z); ndarray (3,)":
    x, y, z = xyz #Unpacking x, y, and z
    dx = -y - z
    dy = x + a*y
    dz = b + z*(x - c)
    return np.array([dx, dy, dz])

dt = 0.01 #Temporal psuedo-dimension
stepnum = 10000

points = np.empty((stepnum + 1, 3)) #1 more for initial value, and 3 for the x, y, and z
points[0] = xyz0
for i in range(stepnum):
    points[i+1] = points[i] + diffeq(points[i]) * dt #Iterating through; Classic Euler method
    continue

#And now onto the best part, plotting!
ax = plt.figure().add_subplot(projection='3d')
ax.plot(*points.T, lw=.5) #Transpose the axes to actually get our coordinates
ax.view_init(elev=elev, azim=azim)
ax.set_xlabel(r'$X\mathrm{\ axis}$')
ax.set_ylabel(r'$Y\mathrm{\ axis}$')
ax.set_zlabel(r'$Z\mathrm{\ axis}$')
ax.set_title(title)
plt.show()
