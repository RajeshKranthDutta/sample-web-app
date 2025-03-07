# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt first to avoid re-installing packages when code changes
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the app
CMD ["python", "app.py"]