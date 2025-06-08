import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# User Inputs
velocity = float(input("Enter initial velocity (m/s): "))
angle_deg = float(input("Enter angle of projection (degrees): "))
angle_rad = np.radians(angle_deg)

# Calculations
T = (2 * velocity * np.sin(angle_rad)) / g  # Time of flight
H = (velocity**2 * np.sin(angle_rad)**2) / (2 * g)  # Maximum height
R = (velocity**2 * np.sin(2 * angle_rad)) / g  # Range

# Display the results
print(f"\nTime of Flight (T): {T:.2f} seconds")
print(f"Maximum Height (H): {H:.2f} meters")
print(f"Range (R): {R:.2f} meters")

# Generate trajectory data
t = np.linspace(0, T, num=100)
x = velocity * np.cos(angle_rad) * t
y = velocity * np.sin(angle_rad) * t - 0.5 * g * t**2

# Plotting the 2D trajectory
plt.plot(x, y, label='Projectile Path')
plt.scatter(x[0], y[0], color='green', label='Start')
plt.scatter(x[-1], y[-1], color='red', label='End')
plt.xlabel('X (Horizontal Distance)')
plt.ylabel('Y (Vertical Height)')
plt.title('2D Projectile Motion')
plt.legend()
plt.show()
