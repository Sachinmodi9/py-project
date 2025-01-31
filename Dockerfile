# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run unit tests during the build process
RUN pytest tests/

# Command to run the application (Modify as needed)
CMD ["python", "app.py"]
