import os
import joblib
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Ensure models folder exists
os.makedirs("lab2/models", exist_ok=True)

# Column names for Car dataset
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]

# Load dataset
data = pd.read_csv("lab2/data/car.csv", names=columns)

# Encode categorical features
label_encoders = {}
for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Split features and target
X = data.drop("class", axis=1)
y = data["class"]

# Train-test split
X_train, _, y_train, _ = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# Save model with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_filename = f"lab2/models/model_{timestamp}.pkl"
joblib.dump(model, model_filename, protocol=5)


print(f"Model saved to {model_filename}")
