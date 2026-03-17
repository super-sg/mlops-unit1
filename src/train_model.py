import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("anime_characters.csv")

print("Columns:", df.columns)

# Keep only relevant numeric columns
df = df[['mal_id', 'favorites']]

# Drop missing values
df = df.dropna()

# Features and target
X = df[['mal_id']]     # feature
y = df['favorites']    # target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\nModel Evaluation:")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "model.pkl")

print("\nModel saved successfully!")