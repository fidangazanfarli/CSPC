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

---

## PW2 - Lab B: Optimization in Chemistry

**1. Optimization Methods Comparison (Part 2):**
- On simple convex functions ($f(x)=(x-3)^2+1$), Gradient Descent, Newton's method, and SLSQP all easily converge to $x = 3.0$[cite: 14].
- On complex/non-convex functions ($g(x)=x^4-3x^2+x+5$), the starting point and method matter significantly: Newton's method solves $g'(x)=0$ and can land on local maxima/saddle points ($g'' < 0$) depending on initialization, while SLSQP and Gradient Descent follow downhill paths toward local or global minima[cite: 14].

**2. Reaction Kinetics Fitting (Part 3):**
- Fitted rate constant: **$k = 0.2618 \text{ s}^{-1}$**[cite: 15].
- Minimizing squared residual error accurately recovers the exponential decay kinetics curve[cite: 15].

**3. Chemical Equilibrium (Part 4):**
- Extent of reaction $x \approx 0.6639$ mol (Newton and SLSQP agree)[cite: 15].
- Equilibrium amounts: $\text{H}_2 = 0.3362 \text{ mol}$, $\text{I}_2 = 0.3362 \text{ mol}$, $\text{HI} = 1.3277 \text{ mol}$[cite: 15].

**4. Titration Equivalence Point (Part 5 - Bonus):**
- Equivalence point detected at **$V = 50.00 \text{ mL}$** where the derivative $\frac{d(\text{pH})}{dV}$ peaks.



---

## PW3 - Session 1: Data Characterisation & Normality Testing

### 1. Dataset Summary
- **Dataset:** Cleveland Heart Disease Dataset (303 patients)[cite: 115].
- **Features Analyzed:** `age`, `chol` (serum cholesterol), `trestbps` (resting blood pressure), `thalach` (maximum heart rate)[cite: 115].

### 2. Variable Shapes & Distributions (`distributions.png`)
- **`age`:** Roughly bell-shaped and symmetric, centered around a mean of ~54.4 years (range: 29–77 years)[cite: 77, 83].
- **`chol`:** Strongly right-skewed with a prominent right tail due to extreme high cholesterol outliers (max: 564.0 mg/dL)[cite: 74, 83].
- **`trestbps`:** Moderately right-skewed, peaking near 120–130 mmHg with occasional severe hypertension readings up to 200 mmHg[cite: 83].
- **`thalach`:** Slightly left-skewed, peaking near 150–160 bpm[cite: 83].

### 3. Normality Check Verdicts
Normality was tested using Q-Q plots (`distributions.png`)[cite: 83, 85] and formal statistical testing via the Shapiro-Wilk test ($\alpha = 0.05$, $H_0$: data is normally distributed)[cite: 100]:

1. **`age`:** **Not Normal** ($W = 0.9865, p = 6.07 \times 10^{-3} < 0.05$). Visually symmetric, but slight deviation from ideal normality[cite: 85, 100].
2. **`chol`:** **Not Normal** ($W = 0.9473, p = 5.91 \times 10^{-9} < 0.05$). Strong right-skewness and heavy tail[cite: 85, 100].
3. **`trestbps`:** **Not Normal** ($W = 0.9665, p = 1.80 \times 10^{-6} < 0.05$). Right-skewed distribution[cite: 85, 100].
4. **`thalach`:** **Not Normal** ($W = 0.9765, p = 7.00 \times 10^{-5} < 0.05$). Left-skewed distribution[cite: 85, 100].






---

## PW3 - Session 2: Statistical Inference & Correlation vs. Causation

### 1. Heart Rate Comparison: Healthy vs. Disease (Task 4)
- **Question:** Do heart-disease patients reach a different maximum heart rate (`thalach`) than healthy ones?
- **Group Statistics:**
  - Healthy Patients (`target = 0`): Mean = **158.38 bpm**, SE = **±1.50 bpm** ($n = 164$).
  - Disease Patients (`target = 1`): Mean = **139.26 bpm**, SE = **±1.92 bpm** ($n = 139$).
- **Hypothesis Testing:**
  - Two-sample t-test: $t = 7.9636$, $p = 3.46 \times 10^{-14}$.
  - Mann-Whitney U test: $U = 16989.5$, $p = 1.86 \times 10^{-13}$.
- **Conclusion:** We strongly reject the null hypothesis $H_0$ ($p \ll 0.05$). Healthy patients achieve a significantly higher maximum heart rate during exercise than heart disease patients. The bar plot with standard error bars (`thalach_comparison.png`) clearly shows non-overlapping uncertainty bounds.

### 2. Age vs. Maximum Heart Rate Relationship (Task 5)
- **Pearson Correlation:** **$r = -0.3938$** ($p = 1.11 \times 10^{-12}$).
- **Interpretation:** There is a strong negative correlation between age and maximum heart rate (`age_vs_thalach.png`). As age increases, achievable peak heart rate decreases steadily by approximately 1 bpm per year.

---

### 3. Chemical-Exposure Mystery: Confounder Reveal (Tasks 6 & 7)

#### Naive Analysis (Task 6)
- **Benzene vs. Malignancy:** $r = 0.3847$ ($p = 1.28 \times 10^{-36}$).
- **Cadmium vs. Malignancy:** **$r = 0.8800$** ($p \approx 0.00$).
- **Naive Conclusion:** Taken at face value, cadmium appears to be the primary cause of tumour malignancy because of its overwhelmingly strong correlation.

#### Controlled Confounder Analysis (Task 7)
- **Identifying the Confounder:** `cadmium` and `pollution_index` are nearly perfectly correlated ($r = 0.9819$), meaning higher industrial pollution environments simply carry higher cadmium levels.
- **Controlling for Pollution:** When restricting analysis to a narrow band of patients with similar pollution exposure ($\text{pollution\_index} \in [47.5, 52.5]$):
  - **Cadmium vs. Malignancy:** $r_{\text{controlled}} = -0.2407$ ($p = 0.0857 > 0.05$, **loses statistical significance**).
  - **Benzene vs. Malignancy:** **$r_{\text{controlled}} = 0.6814$** ($p = 2.70 \times 10^{-8} \ll 0.05$, **remains strongly positive and highly significant**).
- **Causal Reveal:** **Benzene is the true causal agent** driving malignancy. Cadmium only looked guilty because it was heavily confounded by overall industrial pollution. Controlling for the environmental confounder exposed cadmium as innocent and confirmed benzene as the true cause (`chemical_causation.png`).