import streamlit as st
import pickle
import pandas as pd

# Load model
pipe = pickle.load(open(r"E:\WORK\PROJECTS\Diabetes\model.pkl", 'rb'))
feature_order = list(pipe.feature_names_in_)

# ------------------- CUSTOM STYLING -------------------
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        font-family: 'Segoe UI', sans-serif;
    }

    .main-title {
        color: white;
        text-align: center;
        font-size: 50px;
        font-weight: bold;
    }

    .description {
        text-align: center;
        font-size: 18px;
        color: white;
        margin-bottom: 25px;
    }

    /* Card/Frame Style */
    .card {
        background-color: black;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: auto;
    }

    /* Button Style */
    .stButton>button {
        background: linear-gradient(90deg, #1E88E5, #43A047);
        color: white;
        font-size: 18px;
        padding: 12px 25px;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1565C0, #2E7D32);
        transform: scale(1.05);
    }

    /* Input field border */
    .stNumberInput>div>div>input {
        border: 2px solid #1E88E5;
        border-radius: 8px;
        padding: 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>Diabetes Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Enter patient details inside the frame below to check the risk of diabetes.</p>", unsafe_allow_html=True)


st.markdown("<div class='card'>", unsafe_allow_html=True)

input_data = {}

for feature in feature_order:
    fl = feature.lower()

    if fl == "pregnancies":
        input_data[feature] = st.number_input(" **Pregnancies**", min_value=0, step=1)

    elif fl == "glucose":
        input_data[feature] = st.number_input("**Glucose Level**", min_value=0, help="Normal: <140 mg/dL")

    elif fl == "bloodpressure":
        input_data[feature] = st.number_input(" **Blood Pressure**", min_value=0, help="Normal: 80/120 mmHg")

    elif fl == "skinthickness":
        input_data[feature] = st.number_input(" **Skin Thickness**", min_value=0)

    elif fl == "insulin":
        input_data[feature] = st.number_input(" **Insulin Level**", min_value=0)

    elif fl == "bmi":
        input_data[feature] = st.number_input(" **BMI**", min_value=0.0, format="%.1f", help="Normal: 18.5 - 24.9")

    elif fl == "diabetespedigreefunction":
        input_data[feature] = st.number_input(" **Diabetes Pedigree Function**", min_value=0.0, format="%.3f")

    elif fl == "age":
        input_data[feature] = st.number_input(" **Age**", min_value=0, step=1)


if st.button("🔍 Predict"):
    input_df = pd.DataFrame([input_data], columns=feature_order)

    prediction = pipe.predict(input_df)[0]
    probability = pipe.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of diabetes.\n\n**Probability:** {probability:.2f}")
    else:
        st.success(f"✅ Low risk of diabetes.\n\n**Probability:** {probability:.2f}")

st.markdown("</div>", unsafe_allow_html=True)
