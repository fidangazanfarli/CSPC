"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration
  - integrate acceleration back up -> recover position
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Read CSV data
t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

# Differentiation (Part 2)
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.2f} m/s^2")
print(f"Acceleration standard deviation: {np.std(a):.2f} m/s^2")

# Integration back up (Part 4)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print(f"Largest position difference: {max_diff:.4f} m")

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, label="Measured Position", color="blue")
ax1.plot(t, y_rec, "--", label="Reconstructed Position", color="cyan")
ax1.set_ylabel("Position (m)")
ax1.legend()
ax1.grid(True)

ax2.plot(t, v, label="Computed Velocity", color="orange")
ax2.plot(t, v_rec, "--", label="Reconstructed Velocity", color="red")
ax2.set_ylabel("Velocity (m/s)")
ax2.legend()
ax2.grid(True)

ax3.plot(t, a, label="Computed Acceleration", color="purple")
ax3.axhline(-9.81, color="black", linestyle="--", label="True -g (-9.81 m/s²)")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s²)")
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig("motion.png")
print("Saved motion.png successfully.")