#Importing
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Parameters
L1, L2 = 1, 1 #Lengths of pendulum rods in meters
m1, m2 = 1, 1 #Mass of the weight on the bottom in kilograms
tmax, intervals = 30, 1000 #Maximum time and intervals in said time
t1, t2 = 129*np.pi/180, 240*np.pi/180 #Initial angles in radians for theta1 and theta2
g = 9.81 #Gravitational acceleration (meters per second squared)

def pendulum(y0, t, L1, L2, m1, m2):
    theta1, z1, theta2, z2 = y0 #Setting up the initial conditions vector

    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2) #Useful variables to reduce work

    theta1dot = z1 #Setting the derivative of theta1 to z1
    z1dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
             (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2) #Defining the derivative of z1
    theta2dot = z2 #Same thing as above, setting the derivative of theta2 to z2
    z2dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + 
             m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2) #Defining the derivative of z2
    return theta1dot, z1dot, theta2dot, z2dot

t = np.linspace(0, tmax, intervals)
#Initial conditions vector: theta1, dthera1/dt, theta2, dtheta2/dt
y0 = np.array([t1, 0, t2, 0])

#Solving
y = odeint(pendulum, y0, t, args=(L1, L2, m1, m2))

theta1, theta2 = y[:,0], y[:,2]

x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2*np.cos(theta2)

#Plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Time')
ax.set_ylabel('X position')
ax.set_zlabel('Y position')
ax.set_title("3D Representation of the pendulums' movement over time")
pendulum1, = plt.plot(t, x1, y1, color="black")
pendulum2, = plt.plot(t, x2, y2)
ax.legend([pendulum1, pendulum2], ["First/Top Pendulum", "Second/Bottom Pendulum"])
plt.show()

fig1 = plt.figure()
ax1 = fig1.add_subplot()
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("2D Representation of the pendulums' movement")
pendulum3, = plt.plot(x1, y1, color="black")
pendulum4, = plt.plot(x2, y2)
ax1.legend([pendulum3, pendulum4], ["First/Top Pendulum", "Second/Bottom Pendulum"])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Time')
ax.set_ylabel('X position')
ax.set_zlabel('Y position')
ax.set_title("3D Representation of the First pendulum's movement over time")
pendulum1, = plt.plot(t, x1, y1)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Time')
ax.set_ylabel('X position')
ax.set_zlabel('Y position')
ax.set_title("3D Representation of the Second pendulum's movement over time")
pendulum2, = plt.plot(t, x2, y2)
plt.show()

fig1 = plt.figure()
ax1 = fig1.add_subplot()
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("2D Representation of the First pendulum's movement")
pendulum3, = plt.plot(x1, y1)
plt.show()

fig1 = plt.figure()
ax1 = fig1.add_subplot()
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("2D Representation of the Second pendulum's movement")
pendulum3, = plt.plot(x2, y2)
plt.show()