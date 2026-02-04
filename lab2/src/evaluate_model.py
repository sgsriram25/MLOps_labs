import os
import joblib
import glob
from datetime import datetime
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Ensure metrics folder exists
os.makedirs("lab2/metrics", exist_ok=True)

# Find the latest model in lab2/models/
model_files = glob.glob("lab2/models/*.pkl")
if not model_files:
    raise FileNotFoundError("No model found in lab2/models/")
latest_model_file = max(model_files, key=os.path.getctime)

# Load the latest model
model = joblib.load(latest_model_file)
print(f"Loaded model: {latest_model_file}")

# Generate synthetic test dataset
X_test, y_test = make_classification(n_samples=100, n_features=5, random_state=42)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1 Score:", f1)
print("Confusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

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
