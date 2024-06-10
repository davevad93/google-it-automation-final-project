#!/usr/bin/env python3

# import required modules
from os import listdir, path
import requests

# Directory with text files
FILES_DIR = "supplier-data/descriptions/"
# URL for uploading data
UPLOAD_URL = "http://localhost/fruits/"

# Get the list of text files
files = [path.join(FILES_DIR, file) for file in listdir(FILES_DIR) if file.endswith(".txt")]

def get_files(file_path):
    """Reads a text file and returns a dictionary with the data."""
    # Get the file ID and the image name
    file_id = path.splitext(path.basename(file_path))[0]
    image_name = f"{file_id}.jpeg"

    # Read the text file and split the lines
    with open(file_path) as file:
        lines = file.read().strip().splitlines()
    name, weight, description = lines

    # Format the weight as an integer
    weight = int(weight.replace(" lbs", ""))

    # Create a dictionary with the data
    data = {
        "name": name,
        "weight": weight,
        "description": description,
        "image_name": image_name
    }
    return data

# Iterate over each text file and upload data
for file_path in files:
    data = get_files(file_path)
    response = requests.post(UPLOAD_URL, json=data)
    if response.ok:
        print("Data uploaded successfully.")
    else:
        print(f"Error: {response.status_code}")
        