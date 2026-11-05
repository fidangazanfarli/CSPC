"""
PW4 Session A -- Concrete Strength Supervised Machine Learning
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# 1. Load data from local path
df = pd.read_csv("data/concrete.csv")

X = df.drop(columns=["strength"])
y = df["strength"]

# 2. Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standard Scaling for KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("=== Part A: Regression (Predicting Strength) ===")

# (1) KNN Regressor
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train_scaled, y_train)
y_pred_knn = knn_reg.predict(X_test_scaled)
rmse_knn = np.sqrt(mean_squared_error(y_test, y_pred_knn))
r2_knn = r2_score(y_test, y_pred_knn)
print(f"KNN Regressor (k=5):   RMSE = {rmse_knn:.3f} MPa | R2 = {r2_knn:.3f}")

# (2) Decision Tree Regressor
tree_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
tree_reg.fit(X_train, y_train)
y_pred_tree = tree_reg.predict(X_test)
rmse_tree = np.sqrt(mean_squared_error(y_test, y_pred_tree))
r2_tree = r2_score(y_test, y_pred_tree)
print(f"Decision Tree (d=5):  RMSE = {rmse_tree:.3f} MPa | R2 = {r2_tree:.3f}")

# Plot Regression Fit
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred_tree, alpha=0.7, color="teal", label="Decision Tree")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", label="Ideal (y=x)")
plt.xlabel("Actual Strength (MPa)")
plt.ylabel("Predicted Strength (MPa)")
plt.title("Actual vs. Predicted Concrete Compressive Strength")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("regression_fit.png")
print("[+] Saved regression_fit.png")


print("\n=== Part B: Classification (Grade >= 35 MPa) ===")

# Binary Classification Target
y_clf = (y >= 35.0).astype(int)

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_clf, test_size=0.2, random_state=42)
X_train_c_scaled = scaler.fit_transform(X_train_c)
X_test_c_scaled = scaler.transform(X_test_c)

# KNN Classifier
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train_c_scaled, y_train_c)
y_pred_knn_c = knn_clf.predict(X_test_c_scaled)
acc_knn = accuracy_score(y_test_c, y_pred_knn_c)

# Decision Tree Classifier
tree_clf = DecisionTreeClassifier(max_depth=5, random_state=42)
tree_clf.fit(X_train_c, y_train_c)
y_pred_tree_c = tree_clf.predict(X_test_c)
acc_tree = accuracy_score(y_test_c, y_pred_tree_c)

print(f"KNN Classifier Accuracy:          {acc_knn * 100:.2f}%")
print(f"Decision Tree Classifier Accuracy: {acc_tree * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test_c, y_pred_tree_c)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["< 35 MPa", ">= 35 MPa"])
fig, ax = plt.subplots(figsize=(6, 5))
disp.plot(ax=ax, cmap="Blues")
plt.title("Confusion Matrix (Decision Tree Classifier)")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("[+] Saved confusion_matrix.png")


print("\n=== Part C: Feature Importance ===")

importances = tree_reg.feature_importances_
feature_imp_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print(feature_imp_df.to_string(index=False))

plt.figure(figsize=(8, 5))
plt.barh(feature_imp_df["Feature"][::-1], feature_imp_df["Importance"][::-1], color="navy", alpha=0.8)
plt.xlabel("Feature Importance")
plt.title("Concrete Ingredient Importance (Decision Tree)")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("feature_importance.png")
print("[+] Saved feature_importance.png")