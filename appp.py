import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

# Title
st.title("Heart Disease Prediction")

st.markdown("Enter the following details to predict the likelihood of heart disease.")

# Input form
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200)
chol = st.number_input("Cholesterol (chol)", min_value=100, max_value=600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", min_value=60, max_value=220)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=6.0, step=0.1)
slope = st.selectbox("Slope of ST segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Prediction button
if st.button("Predict"):
    input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_features)[0]
    
    if prediction == 1:
        st.error("🚨 The person **has Heart Disease**.")
    else:
        st.success("✅ The person **does NOT have Heart Disease**.")
