import numpy as np
import matplotlib.pyplot as plt


#Nice funcs
#y**2 / (x+.01)
#2*x*y
#4 * x**(1/2) * y
def f(x,y):
    return int(2)*int(x)*int(y)

x0 = 1
xnum = 50
y = range(50)
numlevels = 2500
cmap="viridis"

plt.rcParams["mathtext.fontset"] = 'cm'


#We want to set y up as a constant whilst iterating through various values for y
#And then we take the resulting differential equation and discretize / iterate through
#Thus we also need an x0?

def solve2var(f, x0: float, y: list, xnum: int = 10):
    fvals = []
    for yi in range(len(y)):
        fvals.append([])
        yn = y[yi] # smiley face from benjamin
        xn = x0
        for xi in range(xnum):
            xn = int(f(xn, yn))
            fvals[yi].append(xn)
    return fvals

def getaccuratelog10(n, e = 300):
    multiplier = 0
    while n > int(10**308):
        n = int(int(n) // int(10)**(int(e)))
        multiplier += 1
    return(np.log10(np.float64(n)) + int(multiplier)*int(e))

sol = solve2var(f, x0, y, xnum)
#print(sol)
for xi, xn in enumerate(sol):
    for yi, yn in enumerate(xn):
        sol[xi][yi] = getaccuratelog10(yn + int(1))
sol = np.array(sol)

levels = np.linspace(sol.min(), sol.max() + 1, numlevels)

plt.subplots()
plt.contourf(range(xnum), y, sol, levels=levels, cmap=cmap)
plt.xlabel("$x$-axis")
plt.ylabel("$x$-axis")
plt.title("Plot of $f(x,y)$, $\partial_x f = 2xy$")
plt.colorbar(cmap=cmap)
#plt.savefig('y2(x^-1).png', dpi=2000)
plt.show()


