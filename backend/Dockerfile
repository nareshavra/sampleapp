# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn (production-ready WSGI server)
# Gunicorn is preferred over Flask's built-in server for production
# We bind it to 0.0.0.0 to make it accessible within the Docker network
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "60", "app:app"]