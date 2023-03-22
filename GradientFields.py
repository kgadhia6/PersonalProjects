import numpy as np
import matplotlib.pyplot as plt

#Cool funcs
#x*np.exp(-1 * (x**2 + y**2))
#np.sin(x**2 * y**2)
#np.cos(x**2 * y**2)
#np.sin(x**2 + y**2)
#np.cos(x**2 + y**2)
#np.cos(x*y)
def f(x, y):
    return np.cos(x+y)
spaces = 25
numlevels = 100
colormap = "viridis"
xlimneg = -2
xlimpos = 2
ylimneg = -2
ylimpos = 2


x = np.linspace(xlimneg, xlimpos, spaces)
y = np.linspace(ylimneg, ylimpos, spaces)

plt.rcParams["mathtext.fontset"] = 'cm'

def finite_diff(f, args: (float, float), i: int):
    h = 1e-13
    args = list(args)
    fn = f(*args)
    args[i] += h
    fn2 = f(*args)
    return (fn2 - fn)/h

def grad(f, args: (float, float)):
    delx = finite_diff(f, args, 0)
    dely = finite_diff(f, args, 1)
    return (delx, dely)

def laplace(f, args: (float, float)):
    args = list(args)
    h = 1
    def diff(i):
        if i == 0:
            x,y = args
            return (f(x + 2*h, y) - 2 * f(x,y) + f(x - 2*h, y)) / (4*h**2)
        else:
            x,y = args
            return (f(x, y + 2*h) - 2 * f(x,y) + f(x, y - 2*h)) / (4*h**2)
    del2x = diff(0)
    del2y = diff(1)
    return del2x + del2y


#Notes about why meshgrid is needed for next section
#You create a 2D grid of values for x and y each, must be same shape so that values correspond
#Ex: x[(1,2)] and y[(1,2)] correspond and when taken together represent a point on the coordinate plane
#Thus x and y represent the coordinate values
#Then you compute arrx and arry with the coordinate values of x and y
#Using arrx and arry as the x and y components of each vector, you can then place them on the coordinate grid
#Thus you have a proper vector field
#And arrz is basically showing that it goes toward bright and away from dark

x, y = np.meshgrid(x,y) #You meshgrid it to obtain a coordinate grid that you pass into grad
arrx, arry = grad(f, [x,y])
arrz = f(x,y) #Sets up colormap
arrlaplace = laplace(f, (x,y)) #Compute Laplacian (i.e divergence of the gradient)

levels = np.linspace(arrz.min(), arrz.max(), numlevels)

fig = plt.quiver(x, y, arrx, arry, zorder=3)
plt.contourf(x, y, arrz, levels=levels, cmap=colormap, zorder=2)
plt.colorbar(cmap=colormap)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Vector field of " + r'$\nabla f\/(x,y)$')
plt.show()


levels = np.linspace(arrlaplace.min(), arrlaplace.max(), numlevels)

fig2 = plt.contourf(x, y, arrlaplace, levels=levels, cmap=colormap)
plt.colorbar(cmap=colormap)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title(r'$\nabla^2 f\/(x,y)$')
plt.show()


