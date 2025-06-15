import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 9.81          # Gravity (m/s^2)
mass = 1.0        # Mass of object (kg)
k = 0.1           # Air resistance coefficient
dt = 0.02         # Time step (s)
y = 100.0         # Initial height (meters)
v = 0.0           # Initial velocity (m/s)

positions = []    # Store y positions

# Update function for simulation
def update(frame):
    global y, v

    # Calculate forces
    Fg = mass * g
    Fd = k * v**2
    Fd *= -1 if v > 0 else 1  # drag opposes motion

    Fnet = Fg + Fd
    a = Fnet / mass

    # Update velocity and position
    v += a * dt
    y -= v * dt  # Going down

    # Store position
    positions.append(y if y > 0 else 0)

    # Stop if it hits ground
    if y <= 0:
        ani.event_source.stop()

    line.set_data(range(len(positions)), positions)
    return line,

# Plot setup
fig, ax = plt.subplots()
ax.set_xlim(0, 500)
ax.set_ylim(0, 110)
line, = ax.plot([], [], lw=2)

ani = animation.FuncAnimation(fig, update, frames=500, interval=20, blit=True)
plt.title("Free Fall with Air Resistance")
plt.xlabel("Time Step")
plt.ylabel("Height (m)")
plt.grid()
plt.show()
