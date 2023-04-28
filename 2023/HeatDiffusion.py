import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import math

plt.rcParams["mathtext.fontset"] = 'stix'

#Paramaters
tmax, dt = 3, .1 #Time control parameters
alpha = 1 #Heat diffusion constant
gridspaces = 10 #gridsize -> size of grid, gridspaces -> amt of grid spaces
u0 = np.zeros((gridspaces, gridspaces))
u0[5,:] = 40000

cmap = plt.colormaps["viridis"] #Colourmap
title = r"$\mathrm{2D\ Heat\ Diffusion,\ }\partial_t u = \alpha\nabla^2 u$" #Graph title

def GetNeighbors(M: np.ndarray, i: tuple, diagonals: bool = False) -> (tuple, ..., tuple):
    """
    Obtain the index tuples around the index tuple i in np.ndarray M.
    Will abide by boundary conditions, but is not periodic.
    """
    i0, i1 = i
    neighbors = []
    for n in (-1, 1):
        if i0 + n >= 0 and i0 + n < M.shape[0]:
            neighbors.append((i0 + n, i1))
        if i1 + n >= 0 and i1 + n < M.shape[1]:
            neighbors.append((i0, i1 + n))
        if diagonals:
            for n2 in (-1, 1):
                if i0 + n >= 0 and i0 + n < M.shape[0] and i1 + n2 >= 0 and i1 + n2 < M.shape[1]:
                    neighbors.append((i0 + n, i1 + n2))
    return neighbors

def Discrete2DLaplacian(M: np.ndarray) -> np.ndarray:
    """
    Computes the 2D Laplacian for an np.ndarray M.
    Abides by boundary conditions, but is not periodic.
    
    Filter (5 point stencil):
    0  1  0
    1 -4  1
    0  1  0
    
    In cases where the boundary may cause issues, it will only
    subtract for however many neighbors there are. Thus if there
    are only 2 neighbors, then it will subtract 2 and add the neighbors.
    
    DEPENDENCIES: GetNeighbors
    """
    LM = np.empty((M.shape))
    for i, v in np.ndenumerate(M):
        neighbors = GetNeighbors(M, i)
        result = -len(neighbors) * v
        for neighbor in neighbors:
            result += M[neighbor]
            continue
        LM[i] = result
        continue
    return LM

def CalculateHeats(tsettings: ("max t", "timestep"), params: ("alpha", "u0"), N: int) -> np.ndarray:
    """
    Calculates heat using everything else before packing it into an np.ndarray.
    Output accessing is as follows -> (step, dim0, dim1)
    
    max t -> Self-evident, must be a float
    timestep -> Self-evident, must also be a float less than max t
    alpha -> Diffusion constant, must be a float
    u0 -> Initial conditions, must be an ndarray with shape (N, N)
    N -> size of grid, must be an int
    """
    #Unpacking & Computing Variables
    tmax, dt = tsettings
    alpha, u0 = params
    steps = int(math.floor(tmax / dt))
    #Initialize output array
    heat = np.empty((steps, N, N))
    heat[0] = u0
    #Compute heat
    for t in range(1, steps):
        LU = Discrete2DLaplacian(heat[t-1])
        heat[t] = heat[t-1] + dt * alpha * LU
        continue
    #Compute levels
    levels = np.linspace( heat[0].min(), heat[0].max(), 40 )
    #And then return
    return heat, levels

def plotheat(u_t: np.ndarray, levels) -> mpl.figure.Figure:
    plt.clf()
    
    plt.title(f'{title}')
    plt.xlabel(r'$X\mathrm{\ axis}$')
    plt.ylabel(r'$Y\mathrm{\ axis}$')
    norm = mpl.colors.BoundaryNorm(levels, ncolors=cmap.N)
    
    
    plt.pcolormesh(u_t, cmap=cmap, norm=norm)
    plt.colorbar()
    
    return plt

heat, levels = CalculateHeats((tmax, dt), (alpha, u0), gridspaces)

def animate(i):
    plotheat(heat[i], levels)
    
anim = FuncAnimation(plt.figure(), animate, frames = int(math.floor(tmax / dt) - 5))
anim.save("heatagain.gif")
print("Check it out!")
