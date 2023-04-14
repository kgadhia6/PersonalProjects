import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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

def SIRupdate(S, I, R, DS, DI, DR, beta, gamma, dt) -> (np.ndarray, np.ndarray):
    """
    S, I, R -> np.ndarray
    DS, DI, DR, beta, gamma, dt -> float
    dt is your timestep
    DS, DI, and DR are your diffusion constants
    beta and gamma are SIR parameters
    S, I, and R are you compartments.
    """
    
    #Compute the laplacians first
    LS = DiscretizedLaplacian(S)
    LI = DiscretizedLaplacian(I)
    LR = DiscretizedLaplacian(R)
    
    #Write the updates then. Note: dS is not the same as DS.
    dS = (DS * LS) - beta*I*S / (S + I + R)
    dI = (DI * LI) + beta*I*S / (S + I + R) - gamma*I
    dR = (DR * LR) + gamma*I
    
    S += dS * dt
    I += dI * dt
    R += dR * dt
    return S, I, R

def CreateInitialConditions(gridsize, S0, I0):
    S = np.ones((gridsize, gridsize))
    I = np.zeros((gridsize, gridsize))
    for i in range(I0):
        
        r1, r2 = np.random.randint(0, gridsize), np.random.randint(0, gridsize)
        I[r1, r2] = 1
        S[r1, r2] = 0
    R = np.zeros((gridsize, gridsize))
    return S, I, R

def draw(S, I, R):
    """draw the concentrations"""
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(S, cmap='Greys')
    ax[1].imshow(I, cmap='Greys')
    ax[2].imshow(R, cmap='Greys')
    ax[0].set_title('Susceptible')
    ax[1].set_title('Infected')
    ax[2].set_title('Removed')
    ax[0].axis('off')
    ax[1].axis('off')
    ax[2].axis('off')

def simulate(gridsize, steps, s0, i0, DS, DI, DR, beta, gamma, dt):
    S, I, R = CreateInitialConditions(gridsize, s0, i0)
    draw(S, I, R)
    for t in range(10000):
        S, I, R = SIRupdate(S, I, R, .002, .004, .001, .002, .001, .1)
    draw(S, I, R)
