# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV PYTHONNUNBUFFERED=1

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]




