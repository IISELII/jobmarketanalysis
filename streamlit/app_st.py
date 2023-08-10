import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

def process_input(input_text):
    # Your preprocessing steps like tokenization, padding, etc.
    # Placeholder for now
    return input_text

def decode_prediction(prediction):
    # Convert the prediction to a job title and description
    # Placeholder for now
    return "Sample Job Title"

# Streamlit UI


# Function to interact with FastAPI endpoint
def get_prediction_from_api(data):
    api_url = "http://fastapi_app:8000"
    response = requests.post(f"{api_url}/predict", json=data)
    if response.status_code != 200:
        st.error(f"Failed to get a valid response. Status code: {response.status_code}. Content: {response.text}")
        return
    return response.json()


st.sidebar.title("Navigation")
page = st.sidebar.radio("Choissisez une page", ["Acceuil", "Chercher un Job", "Analyse du marché de l'emploi"])

if page == "Acceuil":
    st.title("Bienvenu sur Job predictor")
    st.write('Naviguez vers la page "Chercher un Job" pour trouver un emploi sur mesure !')

elif page == "Chercher un Job":
    st.title("Trouvez votre job de rêve !")

    # Input fields
    tools = st.text_input("Entrez les outils que vous souhaitez utiliser dans votre travail (sql, powerBI, ...)")
    description = st.text_input("Qu'aimeriez-vous faire dans votre travail (travail d'équipe, gestion d'une équipe...):")

    # Prediction button
    if st.button("Trouvez l'emploi qu'il vous faut !"):
        data = {
            "tools": tools,
            "description": description
        }
        result = get_prediction_from_api(data)
        if result and 'job_title' in result:
            st.write(f"{result['job_title']} est un job qui pourrait vous correspondre")
        else:
            st.write("Failed to get job title.")


elif page == "Analyse du marché de l'emploi":
    st.title("Analyse du marché de l'emploi")
    st.write("Apprenez en plus sur le marché de l'emploi actuelle")
