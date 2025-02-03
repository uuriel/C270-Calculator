#!/bin/bash

echo "Starting Flask Application..."

# Navigate to project directory
cd /var/jenkins_home/workspace/CalculatorBuildApp || exit 1

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is missing! Installing now..."
    apt update && apt install -y python3 python3-pip python3-venv
fi

# Ensure virtual environment is created
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Stop any existing Flask process
fuser -k 3000/tcp || true  # Prevents script failure if port isn't in use

# Start Flask and capture logs
echo "Starting Flask in the background..."
nohup python app.py > flask_output.log 2>&1 &

# Wait for Flask to start
sleep 10

# Check if Flask is running
if ! curl --silent --fail http://172.17.0.1:3000 > /dev/null; then
    echo "❌ Error: Flask failed to start. Logs:"
    cat flask_output.log
    exit 1
fi

echo "✅ Flask started successfully!"
