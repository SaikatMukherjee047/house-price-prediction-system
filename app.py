import pandas as pd

import joblib

model = joblib.load("house_price_model.pkl")

import streamlit as st

st.title("House Price Prediction System")

st.write("Made during the 5th sem ai/ml mini project under the guidance of sir, Kalyan paul ")



gr_liv_area = st.number_input("Living Area (sq ft)")
garage_cars = st.number_input("Garage Capacity")
garage_area = st.number_input("Garage Area")
total_bsmt_sf = st.number_input("Total Basement Area")
full_bath = st.number_input("Numbers of Bathrooms")
bedroom_abv_gr = st.number_input("Number of Bedrooms")
year_built = st.number_input("Year Built")



input_data = pd.DataFrame({
    "GrLivArea":[gr_liv_area],
    "GarageCars":[garage_area],
    "GarageArea":[garage_area],
    "TotalBsmtSF":[total_bsmt_sf],
    "FullBath":[full_bath],
    "BedroomAbvGr":[bedroom_abv_gr],
    "YearBuilt":[year_built]
})

if st.button("Predict Price"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )