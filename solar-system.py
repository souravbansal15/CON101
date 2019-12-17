import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

n = 2               # Number of particles
m = np.ones(n)      # Particle masses
x = np.zeros((n,2)) # Particle positions (x and y for ith particle in x[i,0], x[i,1])
v = np.zeros((n,2)) # Particle velocities
f = np.zeros((n,2)) # Force accumulator
dt = 0.02       # Time step

g = np.array([0,-9.8]) # Acceleration due to gravity

# Initialize
m[0] = 10
m[1] = 0.1
x[0,:] = np.array([0,0])
x[1,:] = np.array([5,0])
v[0,:] = np.array([0,0])
v[1,:] = np.array([-5,10])

# Time stepping (this is actually "semi-implicit Euler")
def step():
    # Accumulate forces on each particle
    f.fill(0)
    #for i in range(n):
    #    f[i,:] += m[i]*g
    f[1,0]=-(50*x[1,0])/(((x[1,0]*x[1,0])+(x[1,1]*x[1,1]))**(1.5))
    f[1,1]=-(50*x[1,1])/(((x[1,0]*x[1,0])+(x[1,1]*x[1,1]))**(1.5))
    # Update velocity of each particle
    #for i in range(n):
    v[1,:] += f[1,:]/m[1] * dt
    # Update position of each particle
    #for i in range(n):
    x[1,:] += v[1,:] * dt

# Drawing code
fig, ax = plt.subplots()
points, = ax.plot(x[0,0], x[0,1], '')

def init():
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)
    ax.set_aspect('equal')
    return points,

def animate(frame):
    step()
    points.set_data(x[:,0], x[:,1])
    if frame is frames-1:
        plt.close()
    return points,

totalTime = 20
frames = int(totalTime/dt)
anim = FuncAnimation(fig, animate, frames=range(frames), init_func=init, interval=dt*1000)
plt.show()
