import os
import joblib
from datetime import datetime
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Ensure models folder exists
os.makedirs("lab2/models", exist_ok=True)

# Generate synthetic dataset
X, y = make_classification(n_samples=500, n_features=5, random_state=42)

# Split dataset 
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)

# Save model with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_filename = f"lab2/models/model_{timestamp}.pkl"
joblib.dump(lr, model_filename)
print(f"Model saved to {model_filename}")
