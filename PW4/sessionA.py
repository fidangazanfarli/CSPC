"""
PW4 Session A -- Tasks A2 & A3: Cleaning, Inspection, and Train-Test Splitting
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

# 1. Load data
df = pd.read_csv("data/concrete.csv")
print(f"Original dataset shape: {df.shape}")

# 2. Task A2: Check duplicates & missing values
duplicates = df.duplicated().sum()
missing_vals = df.isna().sum().sum()
print(f"Duplicate rows found: {duplicates}")
print(f"Missing values found: {missing_vals}")

# Remove duplicates if any exist
df = df.drop_duplicates().reset_index(drop=True)

# Rebuild X and y
X = df.drop(columns=["strength"])
y = df["strength"]

# Summary statistics to inspect numerical scales
print("\n--- Summary Statistics (df.describe()) ---")
print(df.describe())

# Plot relationships (Strength vs Cement & Age)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(df["cement"], y, alpha=0.6, color="teal")
ax1.set_xlabel("Cement (kg/m^3)")
ax1.set_ylabel("Strength (MPa)")
ax1.set_title("Strength vs. Cement")
ax1.grid(True, linestyle="--", alpha=0.5)

ax2.scatter(df["age"], y, alpha=0.6, color="purple")
ax2.set_xlabel("Age (days)")
ax2.set_ylabel("Strength (MPa)")
ax2.set_title("Strength vs. Age")
ax2.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("strength_vs_inputs.png")
print("[+] Saved strength_vs_inputs.png successfully.")


# 3. Task A3: Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n--- Task A3: Split Sizes ---")
print(f"Training set rows: {X_train.shape[0]}")
print(f"Testing set rows:  {X_test.shape[0]}")