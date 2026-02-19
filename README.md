**Lab  - Run Instructions**


- **Prerequisites**: Python 3.8+ and these Python packages:
  - `scikit-learn`
  - `joblib`
  - `numpy`

- **Setup (recommended)**:
  1. Create a virtual environment from the repository root and activate it.

  - Windows (cmd):

    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    ```

  - PowerShell:

# MLOps Lab Repository

## Setup

Before running any labs, complete the setup steps once.

### Step 1: Create and activate a virtual environment

**On Windows (cmd):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Linux or macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 2: Install dependencies

From the repository root, run:

```bash
pip install pandas scikit-learn joblib pytest
```

---

# Lab 1: Calculator Functions and Unit Tests

## Overview

Lab 1 tests four simple calculator functions. The functions are in [lab1/src/calculator.py](lab1/src/calculator.py).

**Functions:**
- `fun1(x, y)` – returns `x + y` (addition)
- `fun2(x, y)` – returns `x - y` (subtraction)  
- `fun3(x, y)` – returns `x * y` (multiplication)
- `fun4(x, y)` – returns `fun1(x, y) + fun2(x, y) + fun3(x, y)` (combination)

## Running Lab 1 Tests

### Step 1: Navigate to the repository root

Make sure you are in the root directory of the project.

### Step 2: Run the tests using pytest

```bash
pytest lab1/test -v
```

This command runs all tests in the `lab1/test` directory with verbose output.

### Step 3: Expected output

All tests should pass. You will see output like:

```
lab1/test/test_pytest.py::test_fun1 PASSED
lab1/test/test_pytest.py::test_fun2 PASSED
lab1/test/test_pytest.py::test_fun3 PASSED
lab1/test/test_pytest.py::test_fun4 PASSED
```

### Alternative: Run tests using unittest

If you prefer unittest instead of pytest, run:

```bash
python -m unittest discover lab1/test -v
```

This will also run all tests and show pass/fail results.

---

# Lab 2: Train and Evaluate a Logistic Regression Model

## Overview

Lab 2 trains a Logistic Regression model on the [Car Evaluation dataset](https://archive.ics.uci.edu/dataset/19/car+evaluation) and evaluates its performance.

**Files:**
- Training script: [lab2/src/train_model.py](lab2/src/train_model.py)
- Evaluation script: [lab2/src/evaluate_model.py](lab2/src/evaluate_model.py)
- Dataset: [lab2/data/car.csv](lab2/data/car.csv)
- Output models: saved to `lab2/models/`
- Output metrics: saved to `lab2/metrics/`

## Running Lab 2

### Step 1: Train the model

From the repository root, run:

```bash
python lab2/src/train_model.py
```

**What happens:**
- Loads the Car Evaluation dataset from `lab2/data/car.csv`
- Encodes all categorical features using `LabelEncoder`
- Splits data into train (80%) and test (20%) sets
- Trains a `LogisticRegression` model on the training set
- Saves the trained model to `lab2/models/model_<timestamp>.pkl`

**Expected output:**
```
Model saved to lab2/models/model_YYYYMMDD_HHMMSS.pkl
```

### Step 2: Evaluate the model

After training completes, run:

```bash
python lab2/src/evaluate_model.py
```

**What happens:**
- Loads the same dataset and applies the same encoding
- Splits data the same way (to get test set)
- Loads the latest model file from `lab2/models/`
- Generates predictions on the test set
- Computes metrics: accuracy, precision, recall, F1-score
- Computes confusion matrix and detailed classification report
- Saves all metrics to `lab2/metrics/metrics_<timestamp>.txt`
- Prints accuracy to console

**Expected output:**
```
Loaded model: lab2/models/model_YYYYMMDD_HHMMSS.pkl
Accuracy: 0.658...
Metrics saved to lab2/metrics/metrics_YYYYMMDD_HHMMSS.txt
```

### Step 3: View the saved metrics

Open the latest metrics file to see detailed results. The file is located at:

```
lab2/metrics/metrics_<timestamp>.txt
```

Each line contains:
- Accuracy score
- Precision score
- Recall score
- F1-score
- Confusion matrix
- Full classification report

Example: See [lab2/metrics/metrics_20260217_184619.txt](lab2/metrics/metrics_20260217_184619.txt) for a sample output.

---

## Troubleshooting

**"No such file or directory: lab2/data/car.csv"**
- Ensure you are running commands from the repository root directory.

**"FileNotFoundError: No model found"**
- Run `python lab2/src/train_model.py` first before running evaluation.

**"ValueError: Model accuracy below acceptable threshold!"**
- The model's accuracy is below 50%. This is intentional behavior to fail CI pipelines. The model may need retraining or the dataset may have changed.
- **sequence** (commands):

**"ModuleNotFoundError: No module named 'sklearn'"**
- Ensure your virtual environment is activated and dependencies are installed:
  ```bash
  pip install pandas scikit-learn joblib pytest
  ```

