import pandas as pd

df = pd.read_parquet("aqora://rigetti/energy-grid-optimization-problem-a/v0.0.0")

print(df.head())
print(f"Dataset shape: {df.shape}")
