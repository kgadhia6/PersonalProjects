#Importing libraries
import numpy as np #Numerical computational library
import matplotlib.pyplot as plt #Plotting library
import sympy as sp #Symbolic computation library

x, y = sp.symbols('x y') #Initialize x & y as variables for sympy

spaces = 25
numlevels = 100
colormap = "viridis"
xlimneg = -4
xlimpos = 4
ylimneg = -4
ylimpos = 4

plt.rcParams["mathtext.fontset"] = 'cm'

fx = sp.cos(x+y) #x (i-hat) component of our vector-valued function
fy = sp.sin(x*y) #y (j-hat) component of our vector-valued function

def getvecs(fx: "expr", fy: "expr") -> "lambda": #noqa to suppress warnings about the function annotations
    lamx = sp.lambdify([x, y], fx, "numpy")
    lamy = sp.lambdify([x, y], fy, "numpy")
    def passargs(x: float, y: float) -> tuple:
        return (lamx(x,y), lamy(x,y))
    return passargs

def divergence(fx: "expr", fy: "expr") -> "lambda 2-var": #Lambdas are functions, expr refers to sympy expressions (noqa)
    dfx, dfy = sp.diff(fx, x), sp.diff(fy, y)
    try:
        lam = sp.lambdify([x,y], (dfx+dfy), "numpy")
        lam(1,2)
        return lam
    except:
        dfx, dfy = sp.differentiate_finite(fx, x), sp.differentiate_finite(fy, y)
        return sp.lambdify([x,y], (dfx + dfy), "numpy")

def curl(fx: "expr", fy: "expr") -> "lambda 2-var": #Lambdas are funcs, expr is from sympy (noqa)
    dyfx, dxfy = sp.diff(fx, y), sp.diff(fy, x)
    try:
        lam = sp.lambdify([x, y], dxfy - dyfx, "numpy")
        lam(1,2)
        return lam
    except:
        dyfx, dxfy = sp.differentiate_finite(fx, y), sp.differentiate_finite(fy, x)
        return sp.lambdify([x,y], dxfy - dyfx)

xd = np.linspace(xlimneg, xlimpos, spaces) #x-axis input domain, 1st member of 2D domain
yd = np.linspace(ylimneg, ylimpos, spaces) #y-axis input domain, 2nd member of 2D domain
xd, yd = np.meshgrid(xd, yd) #Construct 2D input grids from the 1D domains
xr, yr = getvecs(fx, fy)(xd, yd) #Obtain the actual vector field
#Computing the divergence for the whole input domain
div = np.zeros(xd.shape)
for i,v in np.ndenumerate(xd):
    xi, yi = v, yd[i]
    div[i] = divergence(fx, fy)(xi, yi)
    continue
#Computing the curl (rotation) for the whole input domain
rot = np.zeros(xd.shape)
for i, v in np.ndenumerate(xd):
    xi, yi = v, yd[i]
    rot[i] = curl(fx, fy)(xi, yi)
    continue

#Plotting via Matplotlib
plt.quiver(xd, yd, xr, yr, np.sqrt(xr**2 + yr**2), cmap=colormap) #Initial vector field
plt.colorbar(cmap=colormap) #Colorbar
plt.title("Vector field of " + r'$\vec v\/(x,y)$')
plt.xlabel(r'$x$-axis')
plt.ylabel(r'$y$-axis')
plt.show() #Displaying

plt.contourf(xd, yd, div, cmap=colormap, levels=np.linspace(div.min(), div.max() + .01, numlevels)) #Divergence
plt.colorbar(cmap=colormap)
plt.title("Contour plot of " + r'$\nabla\cdot\vec v\/(x,y)$')
plt.xlabel(r'$x$-axis')
plt.ylabel(r'$y$-axis')
plt.show()

plt.contourf(xd, yd, rot, cmap=colormap, levels=np.linspace(rot.min(), rot.max() + .01, numlevels)) #Curl
plt.colorbar(cmap=colormap)
plt.title("Contour plot of " + r'$\nabla\times\vec v\/(x,y)$')
plt.xlabel(r'$x$-axis')
plt.ylabel(r'$y$-axis')
plt.show()

