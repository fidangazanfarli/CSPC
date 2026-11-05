"""
PW4 Task A1 -- Fetch Concrete dataset and save to data/concrete.csv
"""
import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

# 1. Create data/ folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# 2. Fetch dataset from UCI (ID 165)
print("Fetching Concrete dataset...")
concrete = fetch_ucirepo(id=165)

# 3. Inspect metadata and variables
print("=== Metadata ===")
print(concrete.metadata)

print("\n=== Variables Table ===")
print(concrete.variables)

# 4. Extract features & target
X = concrete.data.features.copy()
y = concrete.data.targets

# 5. Rename columns
X.columns = ["cement", "slag", "ash", "water", "superplastic", "coarse_agg", "fine_agg", "age"]
y = y.iloc[:, 0].rename("strength")

# 6. Save combined dataset to data/concrete.csv
X.assign(strength=y).to_csv("data/concrete.csv", index=False)
print("\n[+] Successfully saved renamed dataset to data/concrete.csv!")