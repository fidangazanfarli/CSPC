import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

t0 = time.perf_counter()
simulate_loop(N0, lam)
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
simulate(N0, lam)
t_numpy = time.perf_counter() - t0

speedup = t_loop / t_numpy

print(f"Pure Python loop time: {t_loop:.4f} seconds")
print(f"NumPy vectorized time:  {t_numpy:.4f} seconds")
print(f"NumPy is {speedup:.2f}x faster")