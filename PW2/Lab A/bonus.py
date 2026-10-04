"""
PW2 Lab A -- Bonus: 2D Tracked Trajectory
Read trajectory.csv (time, x, y), compute 2D velocities and speed,
and plot the 2D path and speed vs time."""

import numpy as np
import matplotlib.pyplot as plt

# 1. Read trajectory.csv
t, x, y = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1, unpack=True)

# 2. Compute vx and vy using np.gradient
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# 3. Compute overall speed sqrt(vx^2 + vy^2)
speed = np.sqrt(vx**2 + vy**2)

# 4. Create plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 2D Path (x vs y)
ax1.plot(x, y, "b.-", label="2D Path")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_title("2D Tracked Path")
ax1.grid(True)
ax1.legend()

# Speed vs time
ax2.plot(t, speed, "r-", label="Speed")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Speed (m/s)")
ax2.set_title("Speed over Time")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("trajectory_2d.png")
print("Saved trajectory_2d.png successfully.")