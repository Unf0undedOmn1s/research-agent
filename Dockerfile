# Use an official Python runtime as base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and force stdout/stderr to be unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements first (for caching layers)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port (only if you have a web server / API endpoint)
EXPOSE 8080

# Run your main script
CMD ["python", "main.py"]
