import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
y = np.linspace(0, 100, 1000)

g = 9.8 #m/s^2
vi = 20 #m/s
theta = np.pi/4

u = []
v = []
tt = []

def x(t):
    return vi*np.cos(theta)*t

def y(t):
    return vi*np.sin(theta)*t-0.5*(g*t**2)

for j in range(0,100):
    t = j*0.1
    tt.append(t)
    u.append(x(t))
    v.append(y(t))

ax = plt.figure().add_subplot(projection='3d')
ax.set_ylim(0, 20)
ax.set_xlim(0, 20)
ax.plot(u, v, t)
plt.show()