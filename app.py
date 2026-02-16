import os
import streamlit as st
import pandas as pd
import joblib

# Load trained model

model = joblib.load(os.path.join(os.path.dirname(__file__), "telco_churn_model.joblib"))


st.set_page_config(page_title="Telco Churn Predictor", layout="centered")

st.title("📞 Customer Churn Prediction System")

st.write("Enter customer details below:")

# -------- User Inputs --------

gender = st.selectbox("Gender", ["Female","Male"])
SeniorCitizen = st.selectbox("Senior Citizen", [0,1])
Partner = st.selectbox("Partner", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["Yes","No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["Yes","No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes","No","No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes","No","No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes","No","No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes","No","No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes","No","No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes","No","No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes","No","No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes","No"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 500.0)

# -------- Predict Button --------

if st.button("Predict Churn"):


 sample = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}])

# Probability prediction

 proba = model.predict_proba(sample)[0][1]   # probability of churn
 prediction = "Yes" if proba >= 0.40 else "No"   # custom threshold

 st.subheader("Prediction Result")
 st.write(f"Churn Risk Probability: **{proba*100:.2f}%**")

 if prediction == "Yes":
  st.error("⚠️ High Risk: Customer is likely to CHURN")
 else:
  st.success("✅ Low Risk: Customer is likely to STAY")


