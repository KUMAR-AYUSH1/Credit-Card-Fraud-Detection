import streamlit as st
import requests
url = "http://localhost:8000/predict"
st.title("Credit Card Fraud Detection")

st.sidebar.header("User Input Parameters")
category = st.sidebar.selectbox("Category", ["grocery", "home", "shopping", "travel", "misc", "entertainment", "personal", "health"])
amt = st.sidebar.number_input("Amount", min_value=0.0, step=1.0)
gender = st.sidebar.selectbox("Gender", ["M", "F"])
age = st.sidebar.number_input("Age", min_value=0, max_value=100, step=1,value=19)
day = st.sidebar.selectbox("Day", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
hour = st.sidebar.number_input("Hour (0-23)", min_value=0, max_value=23)
distance_km = st.sidebar.selectbox("Distance Km", ["Local", "Commute", "Regional", "Long_Distance", "Remote"])

data = {
    "category": category,
    "amt": amt,
    "gender": gender,
    "age": age,
    "day": day,
    "hour": hour,
    "distance_km": distance_km
}

if st.button("Check for Fraud"):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json()
            is_fraud = result.get("is_fraud")
            st.write(f"Is Fraud: {is_fraud}")
        else:
            st.write(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write(f"Error: {e}")


st.header("About")
st.write("This app uses a machine learning model to detect credit card fraud.")
st.write("example1 travel,3.37,M,92,Tue,22,Long_Distance  not fraud")
st.write("example2 grocery,49.05,F,32,Mon,14,Local  not fraud")
st.write("example3 misc,868.52,F,29,Sat,1,Regional  is fraud")
st.write("example4 misc,742.73,F,29,Sun,1,Commute  is fraud")
st.write("dataset url : {https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTrain.csv}")