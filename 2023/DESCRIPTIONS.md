EulerDiffEqMethod.py: Plots the solutions of a first order system of ordinary differential equations using the Euler forward step method.
Utilizes numpy and matplotlib.


GradientFields.py: Plots the gradient and Laplacian of a multivariate function that takes in 2 inputs (x, y) and outputs 1 value (z).
Utilizes numpy and matplotlib.


PDEDiscretizer.py: Plots the integration of a partial differential equation in respect to x. If you want to do so in respect to y, just swap the params.
Utilizes numpy and matplotlib.


VectorFields.py: Plots the vector field, divergence, and curl of a vector-valued function.
Utilizes numpy, sympy, and matplotlib.

PhasePortraits3D.py: Plots the 3D vector field of the phase portrait of a 3D system of ordinary differential equations.
Utilizes numpy, and matplotlib.


3DRK4.py: Plots the solutions of a system of ordinary differential equations using an implementation of the 4th order Runge-Kutta algorithm.
Utilizes numpy, and matplotlib.

NewtonianOrbitals.py: Plots the orbits of n-number of planets. Might be a bit numerically unstable, but I pulled an object-oriented approach this time, next time I'll stick to functional programming to see if I can do better.
Utilizes numpy (Generates t, that's all), and matplotlib. Also uses the built-in Python C-math library.

DiffusiveSIR.py: Plots a diffusion based SIR model. Utilizes numpy, and matplotlib. I also used the reference gray-scott diffusion-reaction model in ReferenceMaterials for this heavily. Code just adds a bunch of functions to the console, run the following to actually get something.

```py
help(simulate)
simulate(40, 100, 200, 10, .2, .4, .2, .04, .02, .25)
```
As for what's going on, compile the following latex code as well.
```latex
\textrm{SIR Model with Diffusion}\\
\partial_tS=D_S\nabla^2S-\frac{\beta IS}{N},\\
\partial_tI=D_I\nabla^2I+\frac{\beta IS}{N} - \gamma I,\\
\partial_tR=D_R\nabla^2R+\gamma I,\\
\textrm{Where $D_S$, $D_I$, and $D_R$ are diffusion constants}\\
\textrm{This is a variant of a reaction-diffusion equation}
```

HeatDiffusion.py: Generates a 2D animation of "heat" diffusing across an object, where the equation is that partial derivative of the heat function "u" over time is equal to the laplacian of u. Utilizes numpy, and matpltolib. Also uses the built-in Python C-math library.
