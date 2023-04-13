#Imports
import math
import matplotlib.pyplot as plt
import numpy as np

#Variables
planets = []
dt = .0005
G = 6.6743 * 10**(-11) #Convert to Coulombs constant and treat mass as charge if you want to describe electrostatic interactions
softening_factor = 0

#Classes
class body:
    def __init__(self, mass, pos, v0):
        self.m = mass
        self.x, self.y = pos
        self.vx, self.vy = v0
    
    def __str__(self):
        return f'body: mass = {self.m}; position = {self.position()}; velocity = {self.velocity()}'
    
    def position(self) -> tuple:
        return (self.x, self.y)
    
    def velocity(self) -> tuple:
        return (self.vx, self.vy)
    
    def UpdatePosition(self):
        self.x += self.vx
        self.y += self.vy

#Functions
def hypot(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

def CalcdV(origin: body, attractors: iter) -> tuple:
    #Calculate total force vector
    Fx, Fy = 0, 0
    for attractor in attractors:
        if not attractor == origin:
            mag = G * origin.m * attractor.m / (hypot(origin.position(), attractor.position()) + softening_factor)**2
            dx, dy = attractor.x - origin.x, attractor.y - origin.y
            theta = math.atan2(dy, dx)
            dFx, dFy = mag * math.cos(theta), mag * math.sin(theta)
            Fx += dFx
            Fy += dFy
    #Convert force vector to acceleration via rearrangement of F=ma
    ax, ay = Fx / origin.m, Fy / origin.m
    #And then convert acceleration vector to dv vector via rearrangement of a = dv/dt
    dvx, dvy = ax * dt, ay * dt
    #And then return our dv vector
    return (dvx, dvy)

#Initialize planets
p1 = body(1, (0, 0), (-.000002,0))
p2 = body(0.75, (0, .003), (.000002, 0))
planets.append(p1)
planets.append(p2)

#Now we get on with the show
tset = np.arange(0, 2, dt) #Set up t

#Now we set up the logging array
positions = [[[attractor.x], [attractor.y]] for attractor in planets]
    
for ti, t in enumerate(tset):
    #First up, update positions
    for index, attractor in enumerate(planets):
        v = CalcdV(attractor, planets)
        attractor.vx += v[0]
        attractor.vy += v[1]
        #Now we log information
        positions[index][0].append(attractor.x)
        positions[index][1].append(attractor.y)
        #Then we move onto velocity
    #Then we finally update position
    for attractor in planets:
        attractor.UpdatePosition()
for index, attractor in enumerate(planets):
    plt.scatter(positions[index][0][0], positions[index][1][0])
    plt.plot(positions[index][0], positions[index][1])
plt.show()
