#This is a rip off of https://github.com/benmaier/reaction-diffusion/blob/master/gray_scott.ipynb
#In fact, it's the same code with a few minor changes (None of which are actual changes)
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Discretized 2D Laplacian differential operator done via convolution
def DiscretizedLaplacian(M: np.ndarray, diagonals: bool = False) -> np.ndarray:
    """
    Computes the 2D discretized laplacian as described on Wikipedia (Discrete Laplace Operator)
    All it does is sum up the differences between its neighbors
    If diagonals = True, then it will also see the diagonals as its neighbors as well
    """
    result = -4 * M
    #np.roll(array, (x, y), axis), we use np.roll because it maintains boundaries
    #The reason why axis is a tuple is because we want to conduct it on all of the axes in the tuple
    result += np.roll(M, (0, -1), (0, 1)) #Right neighbor (0, -1)
    result += np.roll(M, (0, 1), (0, 1)) #Left neighbor (0, 1)
    result += np.roll(M, (-1, 0), (0, 1)) #Top neighbor (-1, 0)
    result += np.roll(M, (1, 0), (0, 1)) #Bottom neighbor (1, 0)
    if diagonals:
        result -= 4 * M
        result += np.roll(M, (1, 1), (0, 1))
        result += np.roll(M, (-1, -1), (0, 1))
        result += np.roll(M, (1, -1), (0, 1))
        result += np.roll(M, (-1, 1), (0, 1))
    return result

#Gray-Scott system for an example
def GSupdate(A, B, DA, DB, f, k, dt) -> (np.ndarray, np.ndarray):
    """
    Updates according to Gray-Scott Model.
    DA and DB are diffusion coefficients, f is feed rate, k is kill rate.
    Of course dt is as always our timestep.
    """
    
    #Compute laplacians first
    LA = DiscretizedLaplacian(A)
    LB = DiscretizedLaplacian(B)
    
    #And then update of course! dA is not DA, and dB is not DB
    dA = (DA * LA - A * B**2 + f * (1 - A)) * dt
    dB = (DB * LB + A * B**2 - (k + f) * B) * dt
    
    A += dA
    B += dB
    return A, B

def get_initial_configuration(N, random_influence=0.2):
    """
    Initialize a concentration configuration. N is the side length
    of the (N x N)-sized grid.
    `random_influence` describes how much noise is added.
    """
    
    # We start with a configuration where on every grid cell 
    # there's a lot of chemical A, so the concentration is high
    A = (1-random_influence) * np.ones((N,N)) + random_influence * np.random.random((N,N))
    
    # Let's assume there's only a bit of B everywhere
    B = random_influence * np.random.random((N,N))
    
    # Now let's add a disturbance in the center
    N2 = N//2
    radius = r = int(N/10.0)
    
    A[N2-r:N2+r, N2-r:N2+r] = 0.50
    B[N2-r:N2+r, N2-r:N2+r] = 0.25
    
    return A, B

def draw(A,B):
    """draw the concentrations"""
    fig, ax = plt.subplots(1,2,figsize=(5.65,4))
    ax[0].imshow(A, cmap='Greys')
    ax[1].imshow(B, cmap='Greys')
    ax[0].set_title('A')
    ax[1].set_title('B')
    ax[0].axis('off')
    ax[1].axis('off')

# update in time
delta_t = 1.0

# Diffusion coefficients
DA = 0.16
DB = 0.08

# define feed/kill rates
f = 0.060
k = 0.062

# grid size
N = 200

# simulation steps
N_simulation_steps = 10000

#Actually run it
A, B = get_initial_configuration(200)

for t in range(N_simulation_steps):
    A, B = GSupdate(A, B, DA, DB, f, k, delta_t)
draw(A,B)
