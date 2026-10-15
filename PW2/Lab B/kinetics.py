"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: Read kinetics.csv into arrays t, C
t, C = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1, unpack=True)
C0 = C[0]

# TODO 2: Define total_error(k) = sum of (measured - C0*exp(-k*t))^2
def total_error(k):
    k_val = k[0]
    C_model = C0 * np.exp(-k_val * t)
    return np.sum((C - C_model) ** 2)

# TODO 3: Minimise total_error with scipy.optimize.minimize
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]
print(f"Fitted rate constant k = {fitted_k:.4f} s^-1")

# TODO 4: Plot measured data and fitted curve
plt.figure(figsize=(8, 5))
plt.scatter(t, C, color="red", label="Measured Concentration", zorder=3)
t_fine = np.linspace(min(t), max(t), 200)
plt.plot(t_fine, C0 * np.exp(-fitted_k * t_fine), "b-", label=f"Fitted Model (k = {fitted_k:.4f})")
plt.xlabel("Time (s)")
plt.ylabel("Concentration (M)")
plt.title("First-Order Reaction Kinetics Fit")
plt.legend()
plt.grid(True)
plt.savefig("kinetics.png")
print("Saved kinetics.png successfully.")
