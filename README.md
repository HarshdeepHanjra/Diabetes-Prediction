# Diabetes Prediction System
A simple and elegant web-based **Machine Learning** application that predicts the likelihood of diabetes based on user-provided health information.  
Built using **Python**, with options to run either via **Flask (Web App)** or **Streamlit (Dashboard App)**.

---

## Project Overview
This system uses a trained Machine Learning model (e.g., Decision Tree, Random Forest, or Logistic Regression) to analyze medical parameters and predict whether a person is diabetic or not.  

The user inputs the following details:
- Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin Level  
- Body Mass Index (BMI)  
- Diabetes Pedigree Function  
- Age  

---

## Web Interface Preview

<a https://github.com/HarshdeepHanjra/Diabetes-Prediction/blob/main/webss.png>Website page</a>

A clean, responsive UI featuring:
- Soft gradient background  
- Centered input card with rounded corners  
- Organized form layout for medical inputs  
- Styled prediction button  

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS (custom styling with gradient UI) |
| **Backend (Option 1)** | Flask |
| **Backend (Option 2)** | Streamlit |
| **Model** | Scikit-learn (Decision Tree / Random Forest / Logistic Regression) |
| **Language** | Python |
| **Data Source** | Pima Indians Diabetes Dataset |

---

## 🧠 How It Works

1. Dataset is preprocessed (handling missing values, scaling, etc.).
2. A Machine Learning model is trained to classify diabetes cases.
3. The trained model is saved as a `.pkl` file (e.g., `model.pkl`).
4. The Flask or Streamlit app loads the model and makes predictions based on user input.

---

## 🚀 Setup Instructions

### 🧩 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/diabetes-prediction-system.git
cd diabetes-prediction-system
