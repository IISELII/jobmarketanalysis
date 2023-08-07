from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('model.h5')

# Create the FastAPI app object
app = FastAPI()

# Define your input data structure
class JobData(BaseModel):
    graduation: str
    skills: str
    contract_type: str

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, stranger, from local'}

# Expose the prediction functionality
@app.post('/predict')
def predict_job(job_data: JobData):
    data = job_data.dict()

    # Process your input data here...
    # This is a placeholder. You should implement your preprocessing, tokenization, etc.
    input_array = process_input(data['graduation'], data['skills'], data['contract_type'])
    
    prediction = model.predict(input_array)

    # Convert your prediction to a job title and description
    # This again depends on your model and how you trained it.
    # Placeholder for now.
    job_title, job_description = decode_prediction(prediction)

    return {
        'job_title': job_title,
        'job_description': job_description
    }

def process_input(graduation, skills, contract_type):
    # Placeholder function. You should implement your preprocessing here.
    return np.array([graduation, skills, contract_type]).reshape(1, -1)

def decode_prediction(prediction):
    # Placeholder function to convert model output to readable format.
    return "Sample Job Title", "Sample Job Description"

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
