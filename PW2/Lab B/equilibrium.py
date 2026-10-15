"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: k_imbalance(x) = (2x)^2 / ((a-x)(b-x)) - K
def k_imbalance(x):
    return ((2 * x)**2 / ((a - x) * (b - x))) - K

# TODO 2 (method 1): Root-finding with Newton's method
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): Minimization with SLSQP
def obj_func(x):
    return k_imbalance(x[0])**2

res_slsqp = minimize(obj_func, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Extent x (Newton root-finding): {x_newton:.5f}")
print(f"Extent x (SLSQP minimization): {x_slsqp:.5f}")

# TODO 4: Report equilibrium amounts and plot composition vs extent x
H2_eq = a - x_newton
I2_eq = b - x_newton
HI_eq = 2 * x_newton

print(f"\nEquilibrium Amounts:")
print(f"  H2: {H2_eq:.4f} mol")
print(f"  I2: {I2_eq:.4f} mol")
print(f"  HI: {HI_eq:.4f} mol")

# Plot composition vs extent x
x_vals = np.linspace(0, 0.99, 200)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, a - x_vals, label="H2 (1 - x)", color="blue")
plt.plot(x_vals, b - x_vals, label="I2 (1 - x)", color="green")
plt.plot(x_vals, 2 * x_vals, label="HI (2x)", color="red")

plt.axvline(x_newton, color="black", linestyle="--", label=f"Equilibrium x = {x_newton:.4f}")
plt.xlabel("Extent of Reaction x (mol)")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium: H2 + I2 <=> 2 HI")
plt.legend()
plt.grid(True)

plt.savefig("equilibrium.png")
print("Saved equilibrium.png successfully.")