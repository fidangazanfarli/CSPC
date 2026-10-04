# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW1/Lab A/.

## Setup

Create the environment for a given lab:
`conda env create -f PW1/Lab A/environment.yml`
`conda activate cspc`

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation in Python using both explicit loops and vectorized NumPy operations, with unit tests in pytest and Git version control.

**Speed comparison (loop vs NumPy):**
- loop : 3.7854 s
- numpy : 0.0004 s
- speed-up: 9948.35 x faster

**Tests:** all passing? yes

**Conclusion:**
- Vectorized array operations with NumPy process large datasets drastically faster than standard Python loops.
- Setting up an isolated Conda environment and automated pytest unit tests ensures code reproducibility across different environments. 



------

## PW1 - Lab B: Data, Plotting, and Automation

**Data Summary & Comparison:**
- The observed data follows an exponential decay trend over time.
- Based on the side-by-side plot, the observed data closely matches the analytical exponential decay curve ($N_0 e^{-\lambda t}$), showing high physical accuracy.

**Snakemake Pipeline:**
- The Snakemake pipeline automates figure generation by checking file timestamps and only re-executing `plot.py` when input files (`decay_observed.csv` or `plot.py`) have changed.



---

## PW2 - Lab A: Motion from Tracking Data

**Results:**
- **Mean Acceleration:** -8.58 m/s² (close to expected free-fall acceleration)[cite: 7].

- **Noise Analysis (Part 3):** Numerical differentiation amplifies high-frequency measurement noise (resulting in a high acceleration standard deviation of ~28.72 m/s²), because dividing small noise fluctuations by small time steps ($\Delta t$) creates huge variations[cite: 8]

- **Integration Recovery (Part 4):** Integration acts as a smoother by summing values over time, which causes random noise to cancel out and successfully recovers the original position trajectory to within ~0.78 meters[cite: 8].