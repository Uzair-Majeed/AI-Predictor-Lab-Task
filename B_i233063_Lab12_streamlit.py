import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_model.pkl")

#set title
st.title("Customer Churn Predictor")

# Inputs
tenure = st.number_input("Tenure (months)", min_value=0, max_value=120, value=12)
monthly = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, value=65.0)
total = st.number_input("Total Charges ($)", min_value=0.0, max_value=15000.0, value=780.0)
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

input_df = pd.DataFrame([{
    'tenure': tenure, 'MonthlyCharges': monthly,
    'TotalCharges': total, 'Contract': contract,
    'InternetService': internet
}])

# event listener
if st.button("Predict"):

    pred = model.predict(input_df)[0]
    prob_churn = model.predict_proba(input_df)[0][1]
    prob_stay = 1 - prob_churn

    if pred == 1:
        st.write("Customer will Churn")
        st.write("Probability of Churn:", prob_churn)
    else:
        st.write("Customer will Stay")
        st.write("Probability of Staying:", prob_stay)