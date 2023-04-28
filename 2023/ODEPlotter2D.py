#Imports
import numpy as np #Numerical computational library
import matplotlib.pyplot as plt #Plotting library

#Domain tuples (lower, upper, # of spaces)
xd = (-3, 3, 20)
yd = (-3, 3, 20)

#System parameters
mu = .74

#Solution approximation parameters
dt, stepnum = .1, 100 #time step, number of steps -> end time = dt * stepnum
points = [(2, 2)] #Points to try out -> (x, y)

#System equations
def diffeq(x: float, y: float) -> np.ndarray:
    newx = mu*(x - x**3 / 3 - y) #Right side of differential equation
    newy = x/mu #Right side of differential equation
    return np.array([newx, newy]) #And output of both as an ndarray for functionality

#Graphical parameters
sysname = r"$\mathrm{Van\ der\ Pol\ Oscillator}$" #Write it in matplotlib mathtext
title = sysname + '\n' + fr'$\mu = {mu}$'
colormap = "viridis"
coloramt = 100
plt.rcParams["mathtext.fontset"] = 'stix'

#Unpacking variables
xd, yd = np.linspace(*xd), np.linspace(*yd) #Unpack domain tuples into ndarrays
xd, yd = np.meshgrid(xd, yd) #And then turn them both into a grid

#Calculate our phase space vectors, u & v
u, v = diffeq(xd, yd) #Which then handles that

#Calculating solutions via Forward Euler
def fwdeuler2d(point: tuple, eqsys: callable, dt: float, stepnum: int) -> np.ndarray:
    points = np.empty((stepnum + 1, 2)) #1 more for initial value, 2 for x and y
    points[0] = point
    for i in range(stepnum):
        points[i+1] = points[i] + diffeq(*points[i]) * dt
        continue
    return points

#Plotting of the approximate solutions
ax = plt.figure()
for point in points:
    plt.plot(*fwdeuler2d(point, diffeq, dt, stepnum).T, zorder=3)
    continue

#Plotting of the phase space
plt.quiver(xd, yd, u, v, np.sqrt(u**2 + v**2), cmap=colormap, zorder=2)

#Making the graph presentable & pretty
plt.title(title)
plt.xlabel(r'$X$ axis')
plt.ylabel(r'$Y$ axis')
cbar = plt.colorbar()
cbar.set_label(r'Derivative Magnitude')
plt.xlim(xd.min(), xd.max())
plt.ylim(yd.min(), yd.max())

#And then show!
plt.show()
