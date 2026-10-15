"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: Read titration.csv
V, pH = np.loadtxt("titration.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: Compute slope with np.gradient and find peak with np.argmax
dpH_dV = np.gradient(pH, V)
equiv_idx = np.argmax(dpH_dV)
equiv_V = V[equiv_idx]

print(f"Equivalence point volume: {equiv_V:.2f} mL")

# TODO 3: Plot pH curve and slope side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot pH vs Volume
ax1.plot(V, pH, "b.-", label="pH curve")
ax1.axvline(equiv_V, color="red", linestyle="--", label=f"Equiv Point ({equiv_V:.1f} mL)")
ax1.set_xlabel("Volume of Base Added (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.grid(True)
ax1.legend()

# Plot Slope vs Volume
ax2.plot(V, dpH_dV, "r.-", label="dpH/dV (Slope)")
ax2.axvline(equiv_V, color="blue", linestyle="--", label=f"Peak Slope ({equiv_V:.1f} mL)")
ax2.set_xlabel("Volume of Base Added (mL)")
ax2.set_ylabel("dpH/dV")
ax2.set_title("Titration Derivative (Slope)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("titration.png")
print("Saved titration.png successfully.")