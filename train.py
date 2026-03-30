import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset.csv")

# Split data
X = data.drop("disease", axis=1)
y = data["disease"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved successfully!")
