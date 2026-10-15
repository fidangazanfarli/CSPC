"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

print("=== Part 2A: Easy Convex Function ===")
x0 = 0.0

# (1) Gradient descent by hand
x = x0
lr = 0.1
for _ in range(100):
    x = x - lr * df(x)
print(f"Gradient Descent result from x0=0: x = {x:.4f}")

# (2) Newton's method on df(x)=0
res_newton_f = newton(df, x0, fprime=d2f)
print(f"Newton's method result from x0=0:  x = {res_newton_f:.4f}")

# (3) SLSQP minimizer
res_slsqp_f = minimize(f, x0, method="SLSQP")
print(f"SLSQP result from x0=0:            x = {res_slsqp_f.x[0]:.4f}")


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

def run_2b(start_x):
    print(f"\n--- Part 2B from x0 = {start_x} ---")
    
    # Gradient Descent
    x = start_x
    lr = 0.01
    for _ in range(1000):
        x = x - lr * dg(x)
    print(f"Gradient Descent: x = {x:.4f}")
    
    # Newton's method on dg(x)=0
    res_n = newton(dg, start_x, fprime=d2g)
    curvature = d2g(res_n)
    point_type = "Minimum (d2g > 0)" if curvature > 0 else "Maximum/Saddle (d2g < 0)"
    print(f"Newton's method:  x = {res_n:.4f} | Curvature d2g={curvature:.2f} -> {point_type}")
    
    # SLSQP
    res_s = minimize(g, start_x, method="SLSQP")
    print(f"SLSQP:            x = {res_s.x[0]:.4f}")

run_2b(0.0)
run_2b(2.0)