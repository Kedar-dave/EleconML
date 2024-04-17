import streamlit as st
import joblib

# # Load the trained model
# with open('gs_naive_bayes.pkl', 'rb') as file:
#     gs_naive_bayes = pickle.load(file)
@st.cache_resource
def cache_model():
    return joblib.load('gs_naive_bayes.joblib')
model = cache_model()
# Function to make predictions
def predict_faulty(temperature, pressure, vibration, oil_quality, noise, hours_run):
    # Perform any necessary preprocessing on the input data
    # Make predictions using the loaded model
    prediction = model.predict([[temperature, pressure, vibration, oil_quality, noise, hours_run]])
    return prediction[0]

def main():
    st.title("Gearbox Fault Prediction")
    
    # Input fields
    temperature = st.slider("Temperature (100-200)(Celcius)", min_value=100, max_value=200, step=1)
    pressure = st.slider("Pressure (100-360)(psi)", min_value=100, max_value=360, step=1)
    vibration = st.slider("Vibration (200-500)", min_value=200, max_value=500, step=1)
    oil_quality = st.slider("Oil Quality (1-3)", min_value=1, max_value=3, step=1)
    noise = st.slider("Noise (70-150)(db)", min_value=70, max_value=150, step=1)
    hours_run = st.slider("Hours Run (15000-20000)", min_value=15000, max_value=20000, step=1)
    
    # Button to trigger prediction
    if st.button("Predict"):
        # Perform prediction
        prediction = predict_faulty(temperature, pressure, vibration, oil_quality, noise, hours_run)
        
        # Display prediction result
        if prediction == 1:
            st.write("Gearbox is faulty.")
        else:
            st.write("Gearbox is not faulty.")

if __name__ == "__main__":
    main()
