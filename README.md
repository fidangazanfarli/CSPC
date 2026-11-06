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
  - **Cadmium vs. Malignancy:** **$r_{\text{controlled}} = -0.2407$ ($p = 0.0857 > 0.05$, **loses statistical significance**).
  - **Benzene vs. Malignancy:** **$r_{\text{controlled}} = 0.6814$** ($p = 2.70 \times 10^{-8} \ll 0.05$, **remains strongly positive and highly significant**).
- **Causal Reveal:** **Benzene is the true causal agent** driving malignancy. Cadmium only looked guilty because it was heavily confounded by overall industrial pollution. Controlling for the environmental confounder exposed cadmium as innocent and confirmed benzene as the true cause (`chemical_causation.png`).


---

## PW4 - Session A: Supervised Machine Learning

### 1. Concrete Dataset Setup & Units (Task A1)
- **cement**: Amount of cement (kg/m^3)
- **slag**: Blast furnace slag (kg/m^3)
- **ash**: Fly ash (kg/m^3)
- **water**: Water (kg/m^3)
- **superplastic**: Superplasticizer (kg/m^3)
- **coarse_agg**: Coarse aggregate (kg/m^3)
- **fine_agg**: Fine aggregate (kg/m^3)
- **age**: Curing time (days)
- **strength**: Compressive strength (MPa, Target variable)

### 2. Data Cleaning & Inspection (Task A2)
- **Duplicates & Missing Values:** 
  - Initial rows: 1,030
  - Duplicate rows removed: **25**
  - Final unique rows: **1,005**
  - Missing values: **0**
- **Why Removing Duplicates Before Splitting Matters:** If identical rows are kept prior to an 80/20 split, exact duplicate records can simultaneously end up in both the training set and the testing set. This leads to *data leakage*, causing the model to memorize samples during training and score artificially high on the test set, creating overly optimistic performance metrics.
- **Numerical Scales (df.describe()):** 
  - Features like `coarse_agg` (mean ~974.4) and `fine_agg` (mean ~772.7) operate on scales in the hundreds.
  - Features like `superplastic` (mean ~6.03) and `age` (mean ~45.9) operate on much smaller numerical scales.
  - *Implication:* Algorithms sensitive to feature distance (such as KNN) require standard scaling (StandardScaler) so that large-scale variables do not dominate distance computations.
- **Visual Trends (strength_vs_inputs.png):**
  - **Strength vs. Cement:** Shows a strong positive linear relationship; higher cement concentration per cubic meter consistently yields higher compressive strength.
  - **Strength vs. Age:** Demonstrates rapid strength development during early curing days, leveling out into a wider spread at 365 days.

### 3. Train-Test Split (Task A3)
- Executed via `train_test_split(X, y, test_size=0.2, random_state=42)`.
- **Split Sizes:**
  - Training Set: **804 rows** (80%)
  - Testing Set: **201 rows** (20%)
- `random_state=42` ensures row shuffling is fixed and fully reproducible across all program executions.

### 4. Regression Performance (Predicting Compressive Strength)
- **KNN Regressor (k = 5):** RMSE = 8.512 MPa, R^2 = 0.719
- **Decision Tree Regressor (max_depth = 5):** RMSE = 9.648 MPa, R^2 = 0.639
- **Conclusion:** KNN performed better for regression due to standard feature scaling, which handles continuous recipe ratios effectively (regression_fit.png).

### 5. Classification Performance (Strength Grade >= 35 MPa)
- **KNN Classifier Accuracy:** **83.01%**
- **Decision Tree Classifier Accuracy:** **82.52%**
- **Conclusion:** Both classifiers achieve strong accuracy when predicting whether concrete meets the structural 35 MPa threshold (confusion_matrix.png).

### 6. Feature Importance Analysis
Based on Decision Tree Gini importance (feature_importance.png):
1. **cement (40.99%)**: Primary binding ingredient.
2. **age (34.01%)**: Curing time required for chemical hydration.
3. **water (13.43%)**: Controls the water-to-cement ratio.
- **Key Scientific Finding:** **Cement content and curing age together account for 75% of concrete compressive strength.**

### 4. Linear Regression (Task A4)
- **Method:** Fitted a multi-variable linear regression model (`LinearRegression()`) to predict concrete compressive strength.
- **Metrics (Cleaned Data):**
  - **Train RMSE:** $10.519 \text{ MPa}$ | **Test RMSE:** $9.796 \text{ MPa}$ | **Test MAE:** $7.746 \text{ MPa}$
  - **Train $R^2$:** $0.611$ | **Train Adjusted $R^2$:** $0.607$ | **Test $R^2$:** $0.628$
- **Residual Analysis (`residuals_vs_age.png`):**
  - Plotting test residuals against age on a logarithmic scale reveals a distinct systematic curvature. 
  - **Scientific Takeaway:** A systematic pattern in residuals proves that the relationship between concrete age/ingredients and compressive strength is **non-linear**. A straight linear hyperplane cannot capture the true asymptotic chemical hydration kinetics over time.

### 5. Polynomial Regression - Degrees 1 to 4 (Task A5)
- **Experiment:** Expanded feature spaces using `PolynomialFeatures` combined with `StandardScaler` and `LinearRegression` pipelines.
- **Results Table:**

| Degree | Features ($p$) | Train RMSE | Test RMSE | Train $R^2$ | Train Adjusted $R^2$ | Test $R^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 8 | 10.519 | 9.796 | 0.611 | 0.607 | 0.628 |
| **2** | 44 | 7.287 | 7.455 | 0.813 | 0.803 | 0.784 |
| **3** | 164 | 4.432 | 6.423 | 0.931 | 0.914 | 0.840 |
| **4** | 494 | 2.338 | 30.165 | 0.981 | 0.952 | -2.531 |

- **Which degree would you choose, and why?**
  - **Degree 3** is the optimal choice. It achieves the best generalization performance with a **Test RMSE of $6.423 \text{ MPa}$** and **Test $R^2$ of $0.840$**, capturing the non-linear physics without exploding in complexity.
- **What happens at Degree 4?**
  - With $p = 494$ features for only $n = 804$ training rows, the model severely **overfits**. While Training RMSE drops to a pristine $2.338 \text{ MPa}$, the test error skyrockets (Test RMSE $= 30.165 \text{ MPa}$, Test $R^2 = -2.531$). The model learned noise rather than underlying patterns.
- **Does Adjusted $R^2$ alone protect you from this?**
  - **No.** Although adjusted $R^2$ applies a penalty for model complexity ($p$), it still evaluates training data only. It cannot predict how a heavily parameterized model will fail when confronted with completely unseen test data. An independent test set split is strictly necessary.


  ### 6. Classification: KNN and Decision Tree (Task A6)
- **Target:** Binary classification predicting whether concrete compressive strength reaches structural grade ($\ge 40 \text{ MPa}$). Stratified 80/20 split used to preserve class balance.

#### **KNN Classifier Results ($K=5$):**
- **With StandardScaler:** **84.47%** test accuracy
- **Without StandardScaler:** **78.64%** test accuracy
- **Why Scaling Matters:** KNN relies on Euclidean distance. Unscaled features with large numerical ranges (such as aggregates) would overwhelm features with smaller numerical ranges (such as superplasticizers or age).
- **Multi-Split Stability (Random States 0–4):** 
  - Test Accuracies: `[82.52%, 87.86%, 87.38%, 84.47%, 85.44%]`
  - **Mean Accuracy:** **85.53%** | **Spread (Max - Min):** **5.34%**

#### **Decision Tree Classifier Sweep:**

| `max_depth` | Number of Leaves | Train Accuracy | Test Accuracy |
| :---: | :---: | :---: | :---: |
| **1** | 2 | 0.7464 | 0.7233 |
| **2** | 4 | 0.7464 | 0.7233 |
| **3** | 8 | 0.8240 | 0.8010 |
| **4** | 14 | 0.8653 | 0.8204 |
| **5** | 24 | 0.8896 | 0.8398 |
| **6** | 37 | 0.9066 | 0.8447 |
| **8** | 62 | 0.9672 | 0.8835 |
| **None** | 86 | 0.9976 | 0.8883 |

- **Depth Selection & Generalization:** As depth increases, training accuracy approaches $99.76\%$, while test accuracy peaks around $88.83\%$ for the unlimited tree. Depths around 5–6 offer a strong balance of accuracy and interpretability.
- **Top Two Levels of Decision Tree (`max_depth=2`):**
  - **Root Split:** `age <= 42.00`
  - **Physical Sense:** **Yes, this makes complete physical sense.** Concrete compressive strength development is fundamentally governed by two primary phases: early hydration curing time (`age`) and the fundamental binding mix proportions (`cement` / `superplasticizer`).

  ### 7. Classification Metrics & Threshold Analysis (Task A7)
- **Target Threshold:** Concrete compressive strength $\ge 40 \text{ MPa}$.
- **Saved File:** Metrics table saved to `results/A_metrics.csv`.

#### Model Evaluation Table:
- **KNN ($K=5$):** TP = 57, FP = 13, FN = 19, TN = 117 | Accuracy = **84.47%**, Precision = **81.43%**, Recall = **75.00%**, $F_1$ = **0.7808**
- **Decision Tree ($\text{max\_depth}=5$):** TP = 62, FP = 19, FN = 14, TN = 111 | Accuracy = **83.98%**, Precision = **76.54%**, Recall = **81.58%**, $F_1$ = **0.7898**

#### KNN Threshold Analysis:
- **Threshold 0.3:** TP = 65, FP = 30, FN = 11, TN = 100 | Precision = 0.68, Recall = 0.86
- **Threshold 0.5:** TP = 57, FP = 13, FN = 19, TN = 117 | Precision = 0.81, Recall = 0.75
- **Threshold 0.7:** TP = 43, FP = 9, FN = 33, TN = 121 | Precision = 0.83, Recall = 0.57
- **Threshold 0.9:** TP = 25, FP = 1, FN = 51, TN = 129 | Precision = 0.96, Recall = 0.33

#### Construction Safety & Threshold Selection:
- **False Negative (FN) Danger:** Predicting concrete meets $\ge 40 \text{ MPa}$ when it actually fails is dangerous on a construction site because it leads to structural instability under load. Recall controls FN occurrences.
- **Threshold Recommendation:** Lowering the threshold to $t = 0.3$ increases Recall and minimizes False Negatives, ensuring structural safety at the cost of higher False Positives (economic waste).

### 8. Feature Importance & Domain Knowledge (Task A8 & Bonus)
- **Primary Factors:** Across raw coefficients, standardized coefficients, tree Gini importance, and permutation importance, **cement content** and **curing age** consistently rank as the top two most important predictive features.
- **Correlation vs. Causality:** High feature importance shows strong predictive association within observational data, but it does not imply that arbitrarily altering a single ingredient will guarantee a proportional strength increase without maintaining correct mix proportions.
- **Bonus (Domain Physics):** Incorporating domain physics ($\log(\text{age})$ and water-to-binder ratio $w/b$) allows a standard 8-feature linear model to achieve high test performance without requiring complex high-degree polynomial expansions.