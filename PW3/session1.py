"""
PW3 Session 1 -- Characterising Data & Normality Testing
Dataset: Cleveland Heart Disease
Variables: age, chol, trestbps, thalach
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Load heart.csv (or Heart_disease_cleveland_new.csv)
try:
    df = pd.read_csv("Heart_disease_cleveland_new.csv")
except FileNotFoundError:
    df = pd.read_csv("heart.csv")

print("=== Task 1: Dataset Overview ===")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
print("First 5 rows:")
print(df.head())

# Isolate the four continuous columns
continuous_cols = ["age", "chol", "trestbps", "thalach"]

print("\nSummary Statistics:")
print(df[continuous_cols].describe())

# 2. Visualize Distributions (Histograms & Q-Q Plots)
fig, axes = plt.subplots(4, 2, figsize=(12, 16))

for i, col in enumerate(continuous_cols):
    data = df[col].dropna()
    
    # Left Panel: Histogram
    axes[i, 0].hist(data, bins=20, color="skyblue", edgecolor="black", alpha=0.7)
    axes[i, 0].set_title(f"Histogram: {col}")
    axes[i, 0].set_xlabel(col)
    axes[i, 0].set_ylabel("Frequency")
    axes[i, 0].grid(True, linestyle="--", alpha=0.5)
    
    # Right Panel: Q-Q Plot
    stats.probplot(data, dist="norm", plot=axes[i, 1])
    axes[i, 1].set_title(f"Q-Q Plot: {col}")
    axes[i, 1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("distributions.png")
print("\n[+] Saved distributions.png successfully.")

# 3. Statistical Normality Test (Shapiro-Wilk)
print("\n=== Task 3: Shapiro-Wilk Normality Tests ===")
print(f"{'Variable':<12} | {'W-Statistic':<11} | {'p-value':<12} | {'Verdict'}")
print("-" * 65)

for col in continuous_cols:
    data = df[col].dropna()
    stat, p = stats.shapiro(data)
    
    # A small p-value (< 0.05) rejects H0 (meaning data is NOT normal)
    if p >= 0.05:
        verdict = "Normal (fail to reject H0)"
    else:
        verdict = "Not Normal (reject H0)"
        
    print(f"{col:<12} | {stat:<11.4f} | {p:<12.5e} | {verdict}")