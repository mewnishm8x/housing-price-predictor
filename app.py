import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 Housing Price Predictor")

area = st.number_input("Area (sq ft)")
bedrooms = st.slider("Bedrooms", 1, 10)
bathrooms = st.slider("Bathrooms", 1, 10)
stories = st.slider("Stories", 1, 5)

mainroad = st.selectbox("Main Road", ["Yes", "No"])
furnishing = st.selectbox("Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])

mainroad_val = 1 if mainroad == "Yes" else 0
furnishing_map = {"Furnished": 2, "Semi-Furnished": 1, "Unfurnished": 0}

if st.button("Predict"):
    features = np.array([[area, bedrooms, bathrooms, stories, mainroad_val, furnishing_map[furnishing]]])
    prediction = model.predict(features)[0]

    st.subheader(f"💰 Price: ${prediction:,.2f}")
