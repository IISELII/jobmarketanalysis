import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
# from tensorflow.keras.models import load_model 


# # Load your trained model
# model = load_model('model.h5')

# def get_job_title_and_description(graduation, skills, contract_type):
#     # Convert your inputs into a format suitable for your model here...
#     # Assuming your model takes in a single concatenated string:
#     input_text = ' '.join([graduation, skills, contract_type])
    
#     # Tokenize, pad, and preprocess your input here...
#     # This depends on how you trained your model.
#     # For now, let's assume a simple function process_input does this:
#     processed_input = process_input(input_text)
    
#     # Predict using the model
#     prediction = model.predict(processed_input)

#     # Convert your prediction to a job title and description
#     # This again depends on your model and how you trained it.
#     # For now, let's assume a function decode_prediction does this:
#     job_title, job_description = decode_prediction(prediction)

#     return job_title, job_description

def process_input(input_text):
    # Your preprocessing steps like tokenization, padding, etc.
    # Placeholder for now
    return input_text

def decode_prediction(prediction):
    # Convert the prediction to a job title and description
    # Placeholder for now
    return "Sample Job Title", "Sample Job Description"

# Streamlit UI


# Function to interact with FastAPI endpoint
def get_prediction_from_api(data):
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    return response.json()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Search Job", "Job Market Analysis"])

if page == "Home":
    st.title("Welcome to the Job Predictor!")
    st.write("Navigate to 'Search Job' to find a job tailored for you!")

elif page == "Search Job":
    st.title("Find Your Dream Job!")
    
    # Input fields
    graduation = st.text_input("Enter your graduation:")
    skills = st.text_input("Enter your skills (comma-separated):")
    contract_type = st.text_input("Enter the type of contract you want (e.g. Full-time, Part-time):")
    
    # Prediction button
    if st.button("Find a job for you!"):
        data = {
            "graduation": graduation,
            "skills": skills,
            "contract_type": contract_type
        }
        result = get_prediction_from_api(data)
        st.subheader(f"Job Title: {result['job_title']}")
        st.write(f"Job Description: {result['job_description']}")

elif page == "Job Market Analysis":
    st.title("Job Market Analysis")
    st.write("Learn more about the current job market")


