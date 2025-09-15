import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

MODAL_PATH = "artifacts/model_data4.joblib"

model_data = joblib.load(MODAL_PATH)
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']
col_to_scale = model_data['col_to_scale']


def prepare_df(age, income, loan_amount, loan_tenure_month,
               avg_dpd, credit_utilization_ratio, open_loan_accounts,
               delinquency_ratio, residence_type, loan_purpose,
               loan_type, loan_to_income_ratio):
    # Create input data with EXACT feature names that match training
    input_data = {
        'sanction_amount': 1,  # placeholder values
        'processing_fee': 1,
        'default':1,
        'gst': 1,
        'net_disbursement': 1,
        'loan_tenure_months': loan_tenure_month,
        'age': age,
        'number_of_open_accounts': open_loan_accounts,
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_to_income_ratio': loan_to_income_ratio,
        'delinquency_ratio': delinquency_ratio,
        'average_dpt_per_deliquant_month': avg_dpd,
        'loan_purpose_Education': 1 if loan_purpose == 'Education' else 0,
        'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
        'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
        'residence_type_Rented': 1 if residence_type == 'Rented' else 0,
    }

    # Convert dictionary to DataFrame
    df = pd.DataFrame([input_data])
    df[col_to_scale] = scaler.transform(df[col_to_scale])
    df = df[features]

    return df


def calculate_credit_score(input_df, base_score=300, scale_length=600):
    # Calculate the linear combination
    x = np.dot(input_df.values, model.coef_.T) + model.intercept_

    # Calculate probability using sigmoid function
    default_probability = 1 / (1 + np.exp(-x))
    non_default_probability = 1 - default_probability

    # Calculate credit score
    credit_score = base_score + non_default_probability.flatten() * scale_length

    def get_ratings(score):
        if 300 <= score < 500:
            return "Poor"
        elif 500 <= score < 650:
            return 'Average'
        elif 650 <= score < 750:
            return 'Good'
        elif 750 <= score <= 900:
            return 'Excellent'
        else:
            return 'Undefined'

    rating = get_ratings(credit_score[0])

    # Return probability as percentage, credit score as integer, and rating
    return default_probability.flatten()[0] * 100, int(credit_score[0]), rating


def predict(age, income, loan_amount, loan_tenure_month,
            avg_dpd, credit_utilization_ratio, open_loan_accounts,
            delinquency_ratio, residence_type, loan_purpose,
            loan_type, loan_to_income_ratio):
    input_df = prepare_df(age, income, loan_amount, loan_tenure_month,
                          avg_dpd, credit_utilization_ratio, open_loan_accounts,
                          delinquency_ratio, residence_type, loan_purpose,
                          loan_type, loan_to_income_ratio)

    probability, credit_score, rating = calculate_credit_score(input_df)
    return probability, credit_score, rating
