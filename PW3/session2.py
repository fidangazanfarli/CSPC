"""
PW3 Session 2 -- Drawing Conclusions & Causation Analysis
Tasks 4-5: Heart Disease Dataset
Tasks 6-7: Chemical-Exposure Mystery Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ==========================================
# PART 1: HEART DISEASE DATASET (Tasks 4 & 5)
# ==========================================
try:
    df_heart = pd.read_csv("Heart_disease_cleveland_new.csv")
except FileNotFoundError:
    df_heart = pd.read_csv("heart.csv")

# --- Task 4: thalach Comparison (Healthy vs Disease) ---
healthy_thalach = df_heart[df_heart["target"] == 0]["thalach"].dropna()
disease_thalach = df_heart[df_heart["target"] == 1]["thalach"].dropna()

# Means & Standard Error of the Mean (SE = std / sqrt(n))
mean_h = healthy_thalach.mean()
se_h = healthy_thalach.std(ddof=1) / np.sqrt(len(healthy_thalach))

mean_d = disease_thalach.mean()
se_d = disease_thalach.std(ddof=1) / np.sqrt(len(disease_thalach))

print("=== Task 4: Max Heart Rate Comparison ===")
print(f"Healthy Patients (target=0): Mean = {mean_h:.2f} bpm, SE = {se_h:.2f} bpm (n={len(healthy_thalach)})")
print(f"Disease Patients (target=1): Mean = {mean_d:.2f} bpm, SE = {se_d:.2f} bpm (n={len(disease_thalach)})")

# Hypothesis tests (Parametric t-test & Non-parametric Mann-Whitney U)
t_stat, t_p = stats.ttest_ind(healthy_thalach, disease_thalach)
u_stat, u_p = stats.mannwhitneyu(healthy_thalach, disease_thalach)

print(f"Two-Sample t-test:   t = {t_stat:.4f}, p-value = {t_p:.5e}")
print(f"Mann-Whitney U Test: U = {u_stat:.1f}, p-value = {u_p:.5e}")

# Plot Means with Error Bars (SE)
plt.figure(figsize=(6, 5))
groups = ["Healthy (0)", "Heart Disease (1)"]
means = [mean_h, mean_d]
errors = [se_h, se_d]

plt.bar(groups, means, yerr=errors, capsize=8, color=["mediumseagreen", "indianred"], alpha=0.85)
plt.ylabel("Mean Max Heart Rate (thalach) [bpm]")
plt.title("Max Heart Rate by Health Status (Mean ± SE)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("thalach_comparison.png")
print("[+] Saved thalach_comparison.png successfully.")

# --- Task 5: Age vs thalach Correlation ---
age = df_heart["age"]
thalach = df_heart["thalach"]
r_pearson, p_pearson = stats.pearsonr(age, thalach)

print("\n=== Task 5: Age vs Max Heart Rate Correlation ===")
print(f"Pearson Correlation r = {r_pearson:.4f} (p-value = {p_pearson:.5e})")

plt.figure(figsize=(7, 5))
plt.scatter(age, thalach, color="purple", alpha=0.6, edgecolors="none")
# Add trendline
m, b = np.polyfit(age, thalach, 1)
plt.plot(age, m * age + b, color="black", linestyle="--", label=f"Fit: r = {r_pearson:.2f}")

plt.xlabel("Age (years)")
plt.ylabel("Max Heart Rate (thalach) [bpm]")
plt.title("Age vs. Maximum Heart Rate")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("age_vs_thalach.png")
print("[+] Saved age_vs_thalach.png successfully.")

# ==========================================
# PART 2: CHEMICAL EXPOSURE MYSTERY (Tasks 6 & 7)
# ==========================================
df_chem = pd.read_csv("chemicals_cancer.csv")

# --- Task 6: Naive Analysis ---
r_benz_naive, p_benz_naive = stats.pearsonr(df_chem["benzene"], df_chem["malignancy"])
r_cadm_naive, p_cadm_naive = stats.pearsonr(df_chem["cadmium"], df_chem["malignancy"])

print("\n=== Task 6: Naive Analysis (Chemicals vs Malignancy) ===")
print(f"Benzene vs Malignancy: r = {r_benz_naive:.4f} (p = {p_benz_naive:.5e})")
print(f"Cadmium vs Malignancy: r = {r_cadm_naive:.4f} (p = {p_cadm_naive:.5e})")

# --- Task 7: Confounder Analysis ---
# Restrict to a narrow band of pollution index (e.g. 47.5 to 52.5) to control for pollution
narrow_band = df_chem[(df_chem["pollution_index"] >= 47.5) & (df_chem["pollution_index"] <= 52.5)]

r_benz_ctrl, p_benz_ctrl = stats.pearsonr(narrow_band["benzene"], narrow_band["malignancy"])
r_cadm_ctrl, p_cadm_ctrl = stats.pearsonr(narrow_band["cadmium"], narrow_band["malignancy"])

print("\n=== Task 7: Controlled Analysis (Pollution Index ~50) ===")
print(f"Benzene vs Malignancy (Controlled): r = {r_benz_ctrl:.4f} (p = {p_benz_ctrl:.5e})")
print(f"Cadmium vs Malignancy (Controlled): r = {r_cadm_ctrl:.4f} (p = {p_cadm_ctrl:.5e})")

# Visualizing Confounder Effect
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Naive Cadmium plot
ax1.scatter(df_chem["cadmium"], df_chem["malignancy"], c=df_chem["pollution_index"], cmap="viridis", alpha=0.7)
ax1.set_xlabel("Cadmium Level")
ax1.set_ylabel("Tumour Malignancy")
ax1.set_title("Naive Cadmium vs Malignancy\n(Color = Pollution Index)")
cbar = plt.colorbar(ax1.scatter(df_chem["cadmium"], df_chem["malignancy"], c=df_chem["pollution_index"], cmap="viridis", alpha=0.7), ax=ax1)
cbar.set_label("Pollution Index")

# Controlled Benzene plot
ax2.scatter(narrow_band["benzene"], narrow_band["malignancy"], color="darkorange", alpha=0.8)
ax2.set_xlabel("Benzene Level")
ax2.set_ylabel("Tumour Malignancy")
ax2.set_title("Controlled Benzene vs Malignancy\n(Fixed Pollution Band: 47.5–52.5)")
ax2.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("chemical_causation.png")
print("[+] Saved chemical_causation.png successfully.")