# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /Sujan

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /Sujan/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /Sujan/

# Expose the port Gunicorn will run on
EXPOSE 3000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "Sujan.wsgi:application"]