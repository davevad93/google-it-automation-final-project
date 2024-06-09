#!/usr/bin/env python3

# Import the required modules
from os import listdir, path
from PIL import Image

# Set the images directory
IMG_DIR = "supplier-data/images/"
# Set the variables for image processing
RESIZE_TO = (600, 400)
IMAGE_FORMAT = "JPEG"

# Get the list of images from the directory
images = [img for img in listdir(IMG_DIR) if img.endswith(".tiff")]

# Iterate through the images
for image in images:
    # Open each image using PIL Image
    input_img = Image.open(path.join(IMG_DIR, image))
    # Resize each image to 600x400 pixels
    output_img = input_img.resize(RESIZE_TO)
    # Use convert("RGB") method for converting RGBA to RGB.
    output_img = output_img.convert("RGB")    
    # Change the images extension from .TIFF to .JPEG
    base_img, _ = path.splitext(image)
    # Save the images with new format
    new_img = f"{base_img}.jpeg"
    # Save the images in the same directory
    output_img.save(path.join(IMG_DIR, new_img), IMAGE_FORMAT)
    