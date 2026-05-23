import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("Adult Income Prediction")

age = st.number_input("Age", 18, 100)

hours_per_week = st.number_input("Hours Per Week", 1, 100)

workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc"])

education = st.selectbox("Education", ["Bachelors", "HS-grad"])

marital_status = st.selectbox("Marital Status", ["Never-married", "Married-civ-spouse"])

occupation = st.selectbox("Occupation", ["Tech-support", "Sales"])

relationship = st.selectbox("Relationship", ["Not-in-family", "Husband"])

race = st.selectbox("Race", ["White", "Black"])

gender = st.selectbox("Gender", ["Male", "Female"])

native_country = st.selectbox("Country", ["United-States", "Pakistan"])

if st.button("Predict"):

    data = pd.DataFrame([{
        "age": age,
        "workclass": workclass,
        "fnlwgt": 100000,
        "education": education,
        "educational_num": 10,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }])

    pred = model.predict(data)

    st.success(f"Prediction: {pred[0]}")