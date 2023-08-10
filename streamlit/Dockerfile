# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the Docker image
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pipenv
RUN pip install pipenv

# Install any needed packages specified in Pipfile
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --ignore-pipfile

# Explicitly install matplotlib using pipenv
RUN pipenv install matplotlib

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable (you might need this if interacting with FastAPI running elsewhere)
# ENV API_URL=http://host.docker.internal:8000

# Run the streamlit app when the container launches
CMD ["pipenv", "run", "streamlit", "run", "app_st.py"]
