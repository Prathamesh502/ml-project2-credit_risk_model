# Credit Risk Modeling 🏦💳

## 📌 Overview
This project predicts the likelihood of a loan applicant defaulting on their credit using historical data. The goal is to help banks and financial institutions **minimize lending risk** while ensuring fair access to credit.

I performed **data preprocessing, feature engineering, SMOTE Tomek for class imbalance, EDA, and model evaluation**. To prevent **data leakage**, all transformations were applied separately on `df_train` and `df_test`. Multiple models were tested (Logistic Regression, Random Forest, XGBoost), and **Optuna** was used to fine-tune the Logistic Regression model to maximize **recall**, which was the priority metric.

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn (EDA & visualization)
- Scikit-learn (Logistic Regression, Random Forest, evaluation metrics)
- XGBoost (for comparison)
- Optuna (hyperparameter tuning focused on recall)
- imbalanced-learn (SMOTE Tomek for class imbalance)
- Streamlit (optional demo)

---

## 📂 Project Structure
├── data/         # Raw & cleaned datasets
├── notebooks/    # Jupyter notebooks for EDA & experiments
├── src/          # Scripts (data processing, training, inference)
├── models/       # Saved ML models
├── app.py        # Streamlit app (optional)
├── requirements.txt # Dependencies
└── README.md

---

## 🚀 Features
- **Exploratory Data Analysis (EDA)** to understand feature distributions and correlations.
- **Feature engineering** and **one-hot encoding** of categorical variables.
- Prevented **data leakage** by applying all transformations separately on `df_train` and `df_test`.
- Handled class imbalance using **SMOTE Tomek**.
- Hyperparameter tuning using **Optuna** to maximize **recall** for Logistic Regression.
- Tested multiple models: Logistic Regression (best), Random Forest, XGBoost.
- Model evaluation using recall, precision, F1-score, accuracy, and ROC-AUC.

---

## 🖥️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/credit-risk-modeling.git](https://github.com/yourusername/credit-risk-modeling.git)
    cd credit-risk-modeling
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run notebooks or app:**
    ```bash
    jupyter notebook notebooks/credit_risk_model.ipynb
    ```
    OR
    ```bash
    streamlit run app.py
    ```

---

## 📊 Results
**Best Model:** Logistic Regression (Optuna tuned for recall)

The model's performance was evaluated with a primary focus on **Recall** for the positive class (applicants who default). The results show that the model successfully identified **94%** of actual defaulters, achieving the project's main goal of minimizing financial risk from missed defaults (false negatives).

This high recall came with a precision of **57%**, indicating a business trade-off where some creditworthy applicants might be incorrectly flagged as risky.

### Final Classification Report:
          precision    recall  f1-score   support

     0.0       0.99      0.93      0.96     11392
     1.0       0.57      0.94      0.71      1108

accuracy                           0.93     12500
macro avg       0.78      0.94      0.84     12500
weighted avg       0.96      0.93      0.94     12500


### Key Metrics:
-   **Recall (Class 1.0):** 94%
-   **Precision (Class 1.0):** 57%
-   **F1-score (Class 1.0):** 71%

---

## 📝 Lessons Learned
- Prioritizing **recall** is crucial in financial applications to avoid misclassifying risky applicants.
- **SMOTE Tomek** improves balance while cleaning noisy samples from the majority class.
- **Feature engineering** and avoiding **data leakage** are critical for model reliability.
- **Optuna** provides efficient hyperparameter tuning tailored to the chosen metric.
- Even simple models (like **Logistic Regression**) can outperform complex ones when tuned properly for a specific business objective.

---

## 🙌 Future Improvements
- Deploy as a **REST API** with FastAPI for production-level inference.
- Add **SHAP values** for per-prediction interpretability.
- Automate the retraining pipeline for new credit data.
- Explore **cost-sensitive learning** to assign different penalties for false negatives vs. false positives.
