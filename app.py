import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("LinearRegressionModel.pkl", "rb") as f:
    model = pickle.load(f)

# Load cleaned data (for dropdowns)
car = pd.read_csv("Cleaned Car.csv")

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Prediction App")

# Inputs
name = st.selectbox("Car Model", sorted(car['name'].unique()))
company = st.selectbox("Company", sorted(car['company'].unique()))
fuel_type = st.selectbox("Fuel Type", car['fuel_type'].unique())

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    step=1000
)

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2025,
    step=1
)

# Prediction
if st.button("Predict Price 💰"):
    input_df = pd.DataFrame(
        [[name, company, fuel_type, kms_driven, year]],
        columns=['name', 'company', 'fuel_type', 'kms_driven', 'year']
    )

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ₹ {int(prediction):,}")
