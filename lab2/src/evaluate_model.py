import os
import glob
import joblib
import pandas as pd
from datetime import datetime
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Ensure metrics folder exists
os.makedirs("lab2/metrics", exist_ok=True)

# Column names
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]

# Load dataset
data = pd.read_csv("lab2/data/car.csv", names=columns)

# Encode categorical features
for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

# Split features and target
X = data.drop("class", axis=1)
y = data["class"]

_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Find latest model
model_files = glob.glob("lab2/models/*.pkl")
if not model_files:
    raise FileNotFoundError("No model found in lab2/models/")

latest_model_file = max(model_files, key=os.path.getctime)
model = joblib.load(latest_model_file)

print(f"Loaded model: {latest_model_file}")

# Predictions
y_pred = model.predict(X_test)

# Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average="weighted", zero_division=0)
rec = recall_score(y_test, y_pred, average="weighted", zero_division=0)
f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=0)

print("Accuracy:", acc)

# Optional: Fail CI if accuracy too low
if acc < 0.50:
    raise ValueError("Model accuracy below acceptable threshold!")

# Save metrics
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
metrics_filename = f"lab2/metrics/metrics_{timestamp}.txt"

with open(metrics_filename, "w") as f:
    f.write(f"Accuracy: {acc}\n")
    f.write(f"Precision: {prec}\n")
    f.write(f"Recall: {rec}\n")
    f.write(f"F1 Score: {f1}\n")
    f.write(f"Confusion Matrix:\n{cm}\n")
    f.write(f"\nClassification Report:\n{report}\n")

print(f"Metrics saved to {metrics_filename}")