import streamlit as st

st.set_page_config(page_title="Weather Prediction App")

# Add the Streamlit components and layout here
import streamlit as st

# Title and description
st.title("Weather Prediction App")
st.markdown("Enter the weather features below and click 'Predict'.")

# Input fields for weather features
precep = st.number_input("Precipitation", min_value=0.0)
temp_max = st.number_input("Max Temperature")
temp_min = st.number_input("Minimum Temperature")
wind = st.number_input("Wind Speed")

# Button to trigger prediction
if st.button("Predict"):
    # Make a POST request to the Flask endpoint ("/predict") to get the prediction
    response = requests.post("http://localhost:5000/predict", json={
        "precep": precep,
        "temp_max": temp_max,
        "temp_min": temp_min,
        "wind": wind
    })

    # Display the prediction result
    if response.status_code == 200:
        prediction = response.json()["prediction_text"]
        st.success(f"The weather of your city is {prediction}")
    else:
        st.error("Failed to get the prediction. Please try again.")
