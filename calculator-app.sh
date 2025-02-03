#!/bin/bash

echo "Starting Flask Application Setup..."

# Create necessary directories for Docker build
mkdir -p tempdir
mkdir -p tempdir/templates
mkdir -p tempdir/static

# Copy the application files into tempdir
echo "Copying application files..."
cp app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# Create Dockerfile
echo "Creating Dockerfile..."
echo "FROM python:3.8" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/app.py" >> tempdir/Dockerfile

# Build the Docker image
cd tempdir
echo "Building Docker image for calculator app..."
docker build -t calculatorapp .

# Run the Docker container
echo "Running Docker container for calculator app..."
docker run -t -d -p 3000:3000 --name calculatorapp_running calculatorapp

# Show running containers
docker ps -a

echo "✅ Calculator App is running inside Docker!"
