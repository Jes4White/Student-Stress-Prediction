import streamlit as st
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("student_stress_model.pkl")
scaler = joblib.load("scaler.pkl")

# Configure page
st.set_page_config(
    page_title="Student Stress Prediction",
    page_icon="🎓",
    layout="centered"
)

# Page title
st.title("🎓 Student Stress Prediction")

# Description
st.write(
    "Enter the student's details below to predict the stress level."
)

st.header("📋 Enter Student Details")
st.subheader("📚 Academic Information")

sleep = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

study = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

social = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

st.subheader("🧠 Psychological Factors")
exam_pressure = st.slider(
    "Exam Pressure",
    min_value=1,
    max_value=10,
    value=5
)

family_support = st.slider(
    "Family Support",
    min_value=1,
    max_value=10,
    value=5
)

st.subheader("ℹ️ Other Information")
month = st.slider(
    "Month",
    min_value=1,
    max_value=12,
    value=6
)
student_type = st.selectbox(
    "Student Type",
    ["College", "School", "Working Student"]
)

# One-Hot Encoding
student_school = 0
student_working = 0

if student_type == "School":
    student_school = 1
elif student_type == "Working Student":
    student_working = 1
# Predict Button
if st.button("Predict Stress Level"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Sleep_Hours": [sleep],
        "Study_Hours": [study],
        "Social_Media_Hours": [social],
        "Attendance": [attendance],
        "Exam_Pressure": [exam_pressure],
        "Family_Support": [family_support],
        "Month": [month],
        "Student_Type_school": [student_school],
        "Student_Type_working_student": [student_working]
    })

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    # Display result
    if prediction[0] == 1:
        st.error("🔴 Prediction: High Stress")
        st.warning(
            "The model indicates that this student may be experiencing a high level of stress."
        )
    else:
        st.success("🟢 Prediction: Low Stress")
        st.info(
            "The model indicates that this student is likely experiencing a relatively lower level of stress."
        )



# Sidebar
st.sidebar.title("About")

st.sidebar.info(
    """
    **Student Stress Prediction**

    This application predicts whether a student is likely to experience
    **High Stress** or **Low Stress** using a Random Forest Machine Learning model.

    **Developed by:**
    Chiranjeet Mishra
    """
)