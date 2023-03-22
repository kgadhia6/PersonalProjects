# 2023Projects
All of the projects I have worked on up to and during 2023 that I am willing to publicly upload. Descriptions of each file are included in the README.md file.

--Project Descriptions--

SEIRQCD.py: 
Compartmental epidemiological model implemented the following compartments & vital dynamics:
 - Susceptible
 - Exposed
 - Infected
 - Recovered
 - Quarantined
 - Carriers
 - & Deceased
Utilizes numpy and matplotlib

PhasePortraits.py:
Plots the phase portrait of a given system of differential equations along with some of the actual solutions.
Utilizes numpy, matplotlib, and scipy.integrate. scipy.integrate is used for the actual solutions, everything else is done via matplotlib

DoublePendulum.py:
Utilization of a second order differential equation solver from scipy to graph the path of a double pendulum given initial conditions.
Utilizes numpy, matplotlib, and scipy.integrate.

PDEDiscretizer.py:
Given a multivariate function (2 inputs, x and y; 1 output, z), it'll integrate it in respect to x and plot it logarithmically.
Where the multivariate function represents the right side of the partial differential equation.
Utilizes numpy, and matplotlib.

GradientFields.py:
Given a multivariate function (2 inputs, x and y; 1 output, z), it'll plot the gradient as a vector field and the divergence of said gradient, also known as the Laplacian of the original function, as a filled contour plot.
Utilizes numpy, and matplotlib.

VectorFields.py:
Given a vector-valued function (2 inputs, x and y; 2 outputs, i and j), it'll plot the vector field of the function, then compute and plot the divergence and curl as filled contour plots. It compute the necessary derivatives symbolically, filling in with finite approximations when the Derivative objects of sympy fail to resolve.
Utilizes numpy, matplotlib, and sympy.
