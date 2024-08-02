# Use the official Python image from the Docker Hub as a base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app/

# Run the Django collectstatic command to collect static files
RUN python manage.py collectstatic --noinput

# Specify the command to run the application
CMD ["gunicorn", "cms.wsgi:application", "--bind", "0.0.0.0:8000"]
