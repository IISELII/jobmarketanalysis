from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from generate import generate_text
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the model and tokenizer
model = load_model('model.h5')

with open("tokenizer.json", "r") as file:
    tokenizer_config = file.read()
    tokenizer = tokenizer_from_json(tokenizer_config)

class JobData(BaseModel):
    tools: str
    description: str

@app.get('/')
def index():
    return {'message': 'Hello, stranger, from local'}

@app.post('/predict')
def predict_job(job_data: JobData):
    try:
        data = job_data.dict()

        # Tokenize tools and description separately and ensure they produce single sequences
        tools_sequence = tokenizer.texts_to_sequences([data['tools']])[0]
        description_sequence = tokenizer.texts_to_sequences([data['description']])[0]

        # Set max_sequence_length according to the model's expected input sizes
        max_sequence_length_tools = 22
        max_sequence_length_description = 21

        # Pad the sequences accordingly
        tools_sequence_padded = pad_sequences([tools_sequence], maxlen=max_sequence_length_tools, padding='post')
        description_sequence_padded = pad_sequences([description_sequence], maxlen=max_sequence_length_description, padding='post')

        generated_text = generate_text([tools_sequence_padded, description_sequence_padded])

        return {
            'job_title': generated_text
        }


    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
