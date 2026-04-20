# AI Lab 11 — Linear & Logistic Regression

## Tasks Overview

| Task | Topic | Dataset |
|------|-------|---------|
| 1 | Linear Regression from Scratch (BGD) | Salary Data (CSV) |
| 2 | Linear Regression using Sklearn | Salary Data (CSV) |
| 3 | Multivariate Linear Regression | California Housing (sklearn built-in) |
| 4 | Logistic Regression from Scratch (BGD) | Breast Cancer Wisconsin (sklearn built-in) |
| 5 | Customer Churn Prediction (Streamlit App) | Telco Customer Churn (CSV) |

## Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install numpy pandas matplotlib seaborn scikit-learn joblib streamlit ipykernel

# Register Jupyter kernel
python -m ipykernel install --user --name=venv --display-name="Python (venv)"
```

## How to Run

### Tasks 1–4 (Notebook)
Open `B_i233063_Lab12.ipynb` in Jupyter, select the **Python (venv)** kernel, and run all cells.

### Task 5 (Streamlit App)
1. Run the **Training Script** cell in the notebook first — this creates `churn_model.pkl`.
2. Then launch the Streamlit app:
```bash
streamlit run B_i233063_streamlit_app.py
```

## Datasets
- `Salary_Data.csv` — [Kaggle](https://www.kaggle.com/datasets/karthickveerakumar/salary-data-simple-linear-regression)
- `WA_Fn-UseC_-Telco-Customer-Churn.csv` — [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- California Housing & Breast Cancer — loaded directly via `sklearn.datasets`

## Author
Uzair Majeed — i233063
