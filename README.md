**Lab 2 - Run Instructions**

- **Overview**: concise instructions to run training and evaluation for Lab 2. The scripts generate a synthetic dataset, train a Logistic Regression model, save the model to `lab2/models/`, and evaluate the latest model, saving metrics to `lab2/metrics/`.

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

    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

  - macOS / Linux (bash):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

  2. Install required packages:

  ```bash
  pip install scikit-learn joblib numpy
  ```

  Optionally, create a `requirements.txt` after installing:

  ```bash
  pip freeze > requirements.txt
  ```

- **Run training**:

  From the repository root, run:

  ```bash
  python lab2/src/train_model.py
  ```

  - What happens: A synthetic dataset is generated, a `LogisticRegression` model is trained, and the model file is saved to `lab2/models/model_<timestamp>.pkl`.
  - Output example: `Model saved to lab2/models/model_YYYYMMDD_HHMMSS.pkl`

- **Run evaluation**:

  Ensure at least one model exists in `lab2/models/` (run training first). Then run:

  ```bash
  python lab2/src/evaluate_model.py
  ```

  - What happens: The script finds the latest `.pkl` in `lab2/models/`, loads it, creates a synthetic test set, computes accuracy/precision/recall/F1/confusion matrix, prints results, and writes a metrics file to `lab2/metrics/metrics_<timestamp>.txt`.

- **View the saved artifacts**:
  - Models: list files in `lab2/models/`.
  - Metrics: open the latest file in `lab2/metrics/`.

  Example commands:

  - Windows (cmd):

    ```cmd
    dir lab2\models
    type lab2\metrics\metrics_*.txt
    ```


    

- **Notes & troubleshooting**:
  - `evaluate_model.py` will raise `FileNotFoundError` if no model is present. Run `train_model.py` first.
  - If you see missing-import errors, ensure your virtual environment is active and dependencies are installed.
  - Both scripts use relative paths (e.g., `lab2/models` and `lab2/metrics`), so run commands from repository root to keep behavior consistent.

- ** sequence** (commands):

  ```bash
  python -m venv .venv
  source .venv/bin/activate   # or .venv\Scripts\activate on Windows
  pip install scikit-learn joblib numpy
  python lab2/src/train_model.py
  python lab2/src/evaluate_model.py
  ```

