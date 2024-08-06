#!/bin/bash

# Update package list and install necessary packages
sudo apt update
sudo apt install -y python3-pip python3-venv

# Navigate to the project directory
cd ./public_html/

# Set up a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Run the application with Gunicorn
gunicorn -w 4 -b 217.21.87.186:8000 main:app --daemon
