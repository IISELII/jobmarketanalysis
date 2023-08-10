# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim-buster

# Set environment variables (to ensure that Python output is sent straight to terminal)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install the problematic package separately
RUN pip install zipp==3.16.2

# Install pipenv and dependencies
RUN pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the API when the container launches
CMD ["pipenv", "run", "uvicorn", "fast:app", "--host", "0.0.0.0", "--port", "8000"]
