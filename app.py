import streamlit as st
import numpy as np
import joblib
# Load the model

model = joblib.load("calorie_burn_model.pkl")

# Page config
st.set_page_config(page_title="🔥 Calorie Burn Predictor", layout="centered", page_icon="🔥")

# Custom CSS for better styling and alignment
st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            font-size: 3em;
            color: #ff4b4b;
            margin-bottom: 0;
        }
        .subheader {
            text-align: center;
            color: #bbbbbb;
            margin-bottom: 40px;
        }
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.5em;
            font-weight: bold;
        }
        .result-box {
            background-color: #163d2f;
            padding: 1em;
            border-radius: 10px;
            text-align: center;
            color: #ffffff;
            font-size: 1.2em;
        }
        footer {
            text-align: center;
            color: #888;
            margin-top: 3em;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🔥 Calorie Burn Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Estimate your calorie burn based on your physical attributes and workout details</div>", unsafe_allow_html=True)

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 10, 80, 25)
height = st.slider("Height (cm)", 100, 220, 170)
weight = st.slider("Weight (kg)", 30, 150, 65)
duration = st.slider("Workout Duration (minutes)", 5, 180, 30)
heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 120)
body_temp = st.slider("Body Temperature (°C)", 36.0, 41.0, 37.0)

# Gender mapping
gender_val = 1 if gender == "Male" else 0

# Predict button
if st.button("🎯 Predict Calories Burnt"):
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)[0]
    st.markdown(f"<div class='result-box'>🔥 Estimated Calories Burnt: <strong>{prediction:.2f}</strong> kcal</div>", unsafe_allow_html=True)

# Footer
st.markdown("<footer>Made with ❤️ by Shahwaiz | Powered by Streamlit & XGBoost</footer>", unsafe_allow_html=True)
