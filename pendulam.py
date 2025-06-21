import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Pendulum parameters
g = 9.81      # gravity (m/s^2)
L = 1.0       # length of pendulum (m)
theta0 = np.pi / 4  # initial angle (radians)
omega0 = 0.0        # initial angular velocity

# Time setup
dt = 0.05           # time step (s)
t_max = 20          # total time (s)

# Physics simulation using simple Euler method
theta = theta0
omega = omega0
angles = []

for _ in np.arange(0, t_max, dt):
    alpha = -(g / L) * np.sin(theta)
    omega += alpha * dt
    theta += omega * dt
    angles.append(theta)

# Setup for animation
fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
line, = ax.plot([], [], 'o-', lw=2)

def update(frame):
    x = L * np.sin(angles[frame])
    y = -L * np.cos(angles[frame])
    line.set_data([0, x], [0, y])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(angles), interval=dt*1000, blit=True)
plt.title("Simple Pendulum Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid()
plt.show()
