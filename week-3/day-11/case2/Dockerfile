# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose port and run the application
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
