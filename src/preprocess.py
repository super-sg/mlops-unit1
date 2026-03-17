import pandas as pd

# Load dataset from local file
df = pd.read_csv("data/anime_characters.csv")

# Display dataset structure
print("Dataset Info:\n")
print(df.info())

# Display first 5 rows
print("\nFirst 5 Rows:\n")
print(df.head())

# Display statistical summary
print("\nStatistical Summary:\n")
print(df.describe())

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Show first few rows again (verification)
print("\nPreview of dataset:\n")
print(df.head())

# Save dataset locally
df.to_csv("processed_anime_data.csv", index=False)

print("\nDataset saved successfully!")