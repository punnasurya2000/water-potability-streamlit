# import streamlit as st
# import joblib
# import numpy as np

# # Load model and scaler
# model = joblib.load("water_model.pkl")
# scaler = joblib.load("scaler.pkl")

# st.title("💧 Water Potability Predictor")
# st.markdown("Enter the water quality parameters below to predict if the water is safe to drink.")

# # Input fields
# ph = st.number_input("pH")
# hardness = st.number_input("Hardness")
# solids = st.number_input("Solids")
# chloramines = st.number_input("Chloramines")
# sulfate = st.number_input("Sulfate")
# conductivity = st.number_input("Conductivity")
# organic_carbon = st.number_input("Organic Carbon")
# trihalomethanes = st.number_input("Trihalomethanes")
# turbidity = st.number_input("Turbidity")

# if st.button("Predict Potability"):
#     input_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity,
#                             organic_carbon, trihalomethanes, turbidity]])
#     scaled = scaler.transform(input_data)
#     result = model.predict(scaled)[0]
#     st.success("✅ Potable Water" if result == 1 else "❌ Not Potable Water")
import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("water_model.pkl")
scaler = joblib.load("scaler.pkl")

# Set page configuration
st.set_page_config(page_title="Water Potability Predictor", layout="wide")

# ✅ Fixed background image CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://stateimpactcenter.org/images/general/_metadata/Issues-in-Focus-Ocean-Water-Policy-Safe-Drinking-Water-Act-Image.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("💧 Water Potability Predictor")
st.markdown("Enter the water quality parameters below to predict if the water is safe to drink.")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", value=7.0)
    solids = st.number_input("Solids", value=15000.0)
    sulfate = st.number_input("Sulfate", value=330.0)
    organic_carbon = st.number_input("Organic Carbon", value=12.0)
    trihalomethanes = st.number_input("Trihalomethanes", value=70.0)

with col2:
    hardness = st.number_input("Hardness", value=200.0)
    chloramines = st.number_input("Chloramines", value=7.0)
    conductivity = st.number_input("Conductivity", value=420.0)
    turbidity = st.number_input("Turbidity", value=3.5)

# Predict Button
if st.button("🚀 Predict Potability"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    
    if prediction == 1:
        st.success("✅ This water is **Potable** (Safe for drinking).")
    else:
        st.error("❌ This water is **Not Potable** (Not safe for drinking).")
