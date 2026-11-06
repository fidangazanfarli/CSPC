"""
PW4 Session A -- Tasks A2 & A3: Cleaning, Inspection, and Train-Test Splitting
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score

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

"""
PW4 Session A -- Tasks A4 & A5: Linear and Polynomial Regression
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load data & split
df = pd.read_csv("data/concrete.csv")
X = df.drop(columns=["strength"])
y = df["strength"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
n_train = X_train.shape[0]
p_base = X_train.shape[1]

print("=== Task A4: Linear Regression ===")
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Predictions
y_train_pred = lin_reg.predict(X_train)
y_test_pred = lin_reg.predict(X_test)

# Metrics
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
test_mae = mean_absolute_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)
train_adj_r2 = 1 - (1 - train_r2) * (n_train - 1) / (n_train - p_base - 1)

print(f"Train RMSE: {train_rmse:.3f} MPa | Test RMSE: {test_rmse:.3f} MPa | Test MAE: {test_mae:.3f} MPa")
print(f"Train R2: {train_r2:.3f} | Train Adj R2: {train_adj_r2:.3f} | Test R2: {test_r2:.3f}")

# Residuals Plot vs Age (log scale)
residuals = y_test - y_test_pred
plt.figure(figsize=(8, 5))
plt.scatter(X_test["age"], residuals, alpha=0.7, color="crimson")
plt.axhline(0, color="black", linestyle="--")
plt.xscale("log")
plt.xlabel("Age (days, log scale)")
plt.ylabel("Residuals (True - Predicted, MPa)")
plt.title("Residuals vs. Age (Linear Regression)")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("residuals_vs_age.png")
print("[+] Saved residuals_vs_age.png")


print("\n=== Task A5: Polynomial Regression (Degrees 1 to 4) ===")
results = []
for deg in [1, 2, 3, 4]:
    model = make_pipeline(
        PolynomialFeatures(degree=deg, include_bias=False),
        StandardScaler(),
        LinearRegression()
    )
    model.fit(X_train, y_train)
    p = model[0].n_output_features_
    
    tr_pred = model.predict(X_train)
    te_pred = model.predict(X_test)
    
    tr_rmse = np.sqrt(mean_squared_error(y_train, tr_pred))
    te_rmse = np.sqrt(mean_squared_error(y_test, te_pred))
    tr_r2 = r2_score(y_train, tr_pred)
    te_r2 = r2_score(y_test, te_pred)
    tr_adj_r2 = 1 - (1 - tr_r2) * (n_train - 1) / (n_train - p - 1)
    
    results.append({
        "Degree": deg,
        "Features (p)": p,
        "Train RMSE": round(tr_rmse, 3),
        "Test RMSE": round(te_rmse, 3),
        "Train R2": round(tr_r2, 3),
        "Train Adj R2": round(tr_adj_r2, 3),
        "Test R2": round(te_r2, 3)
    })

df_a5 = pd.DataFrame(results)
print(df_a5.to_string(index=False))


"""
PW4 Session A -- Task A6: KNN and Decision Tree Classification (>= 40 MPa)
"""
# 1. Define Binary Classification Target (Strength >= 40 MPa)
y_class = (df["strength"] >= 40.0).astype(int)

# Stratified split to keep class proportions identical
X_train, X_test, y_train, y_test = train_test_split(
    X, y_class, test_size=0.2, random_state=42, stratify=y_class
)

print("\n=== Task A6: KNN Classifier Sweep ===")
k_values = [1, 3, 5, 7, 15, 25, 51, 101]
knn_train_acc = []
knn_test_acc = []

for k in k_values:
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
    model.fit(X_train, y_train)
    knn_train_acc.append(accuracy_score(y_train, model.predict(X_train)))
    knn_test_acc.append(accuracy_score(y_test, model.predict(X_test)))

# Plot KNN accuracy vs K
plt.figure(figsize=(8, 5))
plt.plot(k_values, knn_train_acc, marker='o', label="Train Accuracy")
plt.plot(k_values, knn_test_acc, marker='s', label="Test Accuracy")
plt.xscale("log")
plt.xlabel("K (number of neighbors, log scale)")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy vs. K (Threshold >= 40 MPa)")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("knn_accuracy_vs_k.png")
print("[+] Saved knn_accuracy_vs_k.png")

# Optimal K comparison (With vs Without Scaler)
optimal_k = 5
model_scaled = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=optimal_k))
model_scaled.fit(X_train, y_train)
acc_with = accuracy_score(y_test, model_scaled.predict(X_test))

model_unscaled = KNeighborsClassifier(n_neighbors=optimal_k)
model_unscaled.fit(X_train, y_train)
acc_without = accuracy_score(y_test, model_unscaled.predict(X_test))

print(f"KNN Test Accuracy (K={optimal_k}) WITH scaler:    {acc_with * 100:.2f}%")
print(f"KNN Test Accuracy (K={optimal_k}) WITHOUT scaler: {acc_without * 100:.2f}%")

# Multi-split evaluation (random_state = 0, 1, 2, 3, 4)
multi_split_accs = []
for rs in [0, 1, 2, 3, 4]:
    Xt_tr, Xt_te, yt_tr, yt_te = train_test_split(
        X, y_class, test_size=0.2, random_state=rs, stratify=y_class
    )
    pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=optimal_k))
    pipe.fit(Xt_tr, yt_tr)
    multi_split_accs.append(accuracy_score(yt_te, pipe.predict(Xt_te)))

print(f"Multi-split Test Accuracies (RS 0-4): {[round(a*100, 2) for a in multi_split_accs]}%")
print(f"Mean Accuracy: {np.mean(multi_split_accs)*100:.2f}% | Spread (Max - Min): {(np.max(multi_split_accs) - np.min(multi_split_accs))*100:.2f}%")


print("\n=== Task A6: Decision Tree Classifier Sweep ===")
depths = [1, 2, 3, 4, 5, 6, 8, None]
tree_results = []

for d in depths:
    tree = DecisionTreeClassifier(criterion="entropy", max_depth=d, min_samples_leaf=1, random_state=0)
    tree.fit(X_train, y_train)
    tr_acc = accuracy_score(y_train, tree.predict(X_train))
    te_acc = accuracy_score(y_test, tree.predict(X_test))
    
    tree_results.append({
        "max_depth": str(d),
        "n_leaves": tree.get_n_leaves(),
        "Train Acc": round(tr_acc, 4),
        "Test Acc": round(te_acc, 4)
    })

df_tree = pd.DataFrame(tree_results)
print(df_tree.to_string(index=False))

# Plot Decision Tree accuracy vs Depth
plt.figure(figsize=(8, 5))
plt.plot([str(d) for d in depths], [r["Train Acc"] for r in tree_results], marker='o', label="Train Accuracy")
plt.plot([str(d) for d in depths], [r["Test Acc"] for r in tree_results], marker='s', label="Test Accuracy")
plt.xlabel("Max Depth")
plt.ylabel("Accuracy")
plt.title("Decision Tree Accuracy vs. Max Depth")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("tree_accuracy_vs_depth.png")
print("[+] Saved tree_accuracy_vs_depth.png")

# Print top two levels of tree (max_depth=2)
tree_depth2 = DecisionTreeClassifier(criterion="entropy", max_depth=2, random_state=0)
tree_depth2.fit(X_train, y_train)
print("\n--- Top Two Levels of Decision Tree (max_depth=2) ---")
print(export_text(tree_depth2, feature_names=list(X.columns)))