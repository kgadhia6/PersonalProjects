#Importing
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
title = ((r'$\mathrm{%s\ via\ RK4}$' % (name)) + "\n" +  r'$a = %.1f,\/ b = %.1f,\/ c = %.1f $' % (a, b, c))

def diffeq(xyz: "3D Coordinate tuple; (x,y,z)") -> np.ndarray:
    x, y, z = xyz
    dx = -y - z
    dy = x + a*y
    dz = b + z*(x - c)
    return np.array([dx, dy, dz])

dt = 0.01 #h
t0 = 0
stepnum = 10000

points = np.empty((stepnum + 1, 3)) #1 more for initial value, and 3 for x, y, and z
time = [None] * (stepnum + 1) #Again, 1 more for initial value
points[0] = xyz0
time[0]
for n in range(stepnum): #RK4 implementation
    pn, tn = points[n], time[n]
    k1 = diffeq(pn)
    k2 = diffeq(pn + (dt * k1) / 2)
    k3 = diffeq(pn + (dt * k2) / 2)
    k4 = diffeq(pn + dt*k3)
    points[n+1] = pn + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt
    continue

#And now onto the best part, plotting!
ax = plt.figure().add_subplot(projection='3d')
ax.plot(*points.T, lw=.5) #Transpose the axes to actually access our coordinates
ax.view_init(elev=elev, azim=azim)
ax.set_xlabel(r'$X\mathrm{\ axis}$')
ax.set_ylabel(r'$Y\mathrm{\ axis}$')
ax.set_zlabel(r'$Z\mathrm{\ axis}$')
ax.set_title(title)
plt.show()
