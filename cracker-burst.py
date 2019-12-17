import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.animation import FuncAnimation



# Time stepping (this is actually "semi-implicit Euler")
def step():
    # Accumulate forces on each particle
    f.fill(0)
    for i in range(n):
        f[i,:] += m[i]*g
    # Update velocity of each particle
    for i in range(n):
        v[i,:] += f[i,:]/m[i] * dt
    # Update position of each particle
    for i in range(n):
        x[i,:] += v[i,:] * dt

def step1():
    # Accumulate forces on each particle
    f.fill(0)
    for i in range(n1):
        f[i,:] += m[i]*g
    # Update velocity of each particle
    for i in range(n1):
        v1[i,:] += f[i,:]/m[i] * dt
    # Update position of each particle
    for i in range(n1):
        y[i,:] += v1[i,:] * dt
    
        

# Drawing code

def init():
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_aspect('equal')
    return points,
flag=False
def animate(frame):
    if frame is frames-1:
        plt.close()
    if(y[0,1]>0):
        step()
        points.set_data(x[:,0], x[:,1],)
        points.set_color("#"+str(random.randint(100000,999999)))
        points1.set_data(-20,-20)
        return points,
    else:
        step1()
        points1.set_data(y[:,0], y[:,1])
        return points1,
    
    
dt = 0.02           # Time step

totalTime = 2
frames = int(totalTime/dt)
for i in range(5):
    
    n = random.randint(5,20)               # Number of particles
    m = np.ones(n)      # Particle masses
    x = np.zeros((n,2)) # Particle positions (x and y for ith particle in x[i,0], x[i,1])
    v = np.zeros((n,2)) # Particle velocities
    f = np.zeros((n,2)) # Force accumulator
   
    g = np.array([0,-9.8]) # Acceleration due to gravity

    n1 = 1
    y = np.zeros((n1,2)) 
    v1 = np.zeros((n1,2))

    # Initialize
    m[0] = 0.1
    x[0,:] = np.array([-10,-10])
    y[0,:] = np.array([0,-5])
    # v[0,:] = np.array([1,4])
    for i in range(n-1):
        v[i,:] =np.array([random.randint(-5,5),random.randint(-5,5)])
    v[n-1,:] = np.array([0,0])
    for i in range(n-1):
        v[n-1,:] -=v[i,:]
    v1[0,:] = np.array([0,10])
    fig, ax = plt.subplots()
    ax.set_facecolor('#87ceeb')
    points, = ax.plot(x[:,0], x[:,1], '*',color="#87ceeb")
    points1, = ax.plot(y[:,0], y[:,1], '^',color="#"+str(random.randint(100000,999999)))
    anim = FuncAnimation(fig, animate, frames=range(frames), init_func=init, interval=dt*1000)
    plt.show()
    time.sleep(2)
    plt.close()
    