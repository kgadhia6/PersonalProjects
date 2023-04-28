#Imports
import numpy as np #Numerical computational library
import matplotlib.pyplot as plt #Plotting library

#Domain for t, calculate dt
td = np.linspace(0, 50, 201)
dt = td[1] - td[0]

#Parameters
init = (1, 1) #x, x'
mu = .74

#Font for graph
plt.rcParams["mathtext.fontset"] = 'cm'

#Functions for computations
def vdp(x, y) -> np.ndarray:
    """
    Computes x and x' for the Van der Pol Differntial Equation.
    See below...
    
    --Actual Differential Equation--
    x'' - mu(1 - x^2)x' + x = 0
    thus, x'' = mu(1-x^2)x' - x
    
    --Splitting it into 2 1st order equations--
    With the actual equations, we can split the equation into 2
    x' = y
    y' = mu(1-x^2)y - x
    """
    dx = y
    dy = mu*(1 - x**2)*y - x
    return np.array([dx, dy])

def fwdeuler(point: tuple, eqsys: callable, dt: float, stepnum: int) -> np.ndarray:
    """
    Integrates differential equation using the forward euler method.
    Use this to generate points to plot a solution curve.
    """
    points = np.empty((stepnum, 2)) #2 to store x and y
    points[0] = point #Load initial value in
    for i in range(stepnum - 1):
        points[i+1] = points[i] + eqsys(*points[i]) * dt
        continue
    return points

#Obtain our x values
x = fwdeuler(init, vdp, dt, len(td))[:,0]

#And now we create our plot
plt.plot(td, x)
plt.title(r'$\mathrm{Van\ der\ Pol\ Oscillator},\ \mu = $' + fr'${mu}$' + '\n' + r"$x^{\prime\prime} - \mu (1-x^2)x^{\prime} + x = 0$")
plt.xlabel(r'$X$ axis')
plt.ylabel(r'Time')

#And then show
plt.show()
