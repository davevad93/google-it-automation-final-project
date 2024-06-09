#!/usr/bin/env python3

# Import the required modules
import requests
from os import listdir, path

# Set the URL for the image upload endpoint
UPLOAD_URL = "http://localhost/upload/"
# Set the directory containing the images
IMG_DIR = "supplier-data/images/"

# Get a list of all the image files in the directory
images = [path.join(IMG_DIR, img) for img in listdir(IMG_DIR) if img.endswith(".jpeg")]

# Function to upload a file
def upload(image, url):
    """Uploads a file to the specified URL."""
    with open(image, "rb") as file:
        requests.post(url, files={"file": file})
        
# Iterate over the image files and upload them
for image in images:
    upload(image, UPLOAD_URL) 
    