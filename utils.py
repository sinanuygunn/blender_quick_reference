from PIL import Image as PILImage
import bpy
import numpy as np
import io
import requests
# Utility functions for image operations

# Downloads an image from a given URL and returns the image data as a BytesIO object.
# If the download fails, returns None.
def download_image(url):
    """
    Download an image from a given URL and return the image data as a BytesIO object.
    
    Args:
        url (str): The URL of the image to download.
        
    Returns:
        BytesIO or None: The downloaded image data as a BytesIO object, or None if the download fails.
    """
    # Set headers for the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Referer": url,
        "DNT": "1" 
    }
    
    # Send a GET request to the URL with the headers
    response = requests.get(url, headers=headers)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Create a BytesIO object from the response content
        image_data = io.BytesIO(response.content)
        return image_data
    
    # If the response status code is not 200, return None
    return None

# Create a bpy.data.images.Image object from image data and return it.
def create_image_from_data(image_data):
    """
    Create a bpy.data.images.Image object from image data and return it.
    
    Args:
        image_data (BytesIO): The image data as a BytesIO object.
        
    Returns:
        bpy.data.images.Image: The created image object.
    """
    # Open the image data as a PIL Image
    pil_image = PILImage.open(image_data)
    
    # Convert the PIL Image to RGBA mode
    pil_image = pil_image.convert("RGBA")
    
    # Convert the PIL Image to a NumPy array
    image_array = np.array(pil_image)
    
    # Create a new bpy.data.images.Image object with the image data
    bpy_image = bpy.data.images.new(name="ClipboardImage", width=pil_image.width, height=pil_image.height)
    
    # Set the pixels of the bpy.data.images.Image object to the pixel data of the PIL Image
    pixels = (image_array.flatten() / 255.0).tolist()
    bpy_image.pixels.foreach_set(pixels) 
    
    # Return the created bpy.data.images.Image object
    return bpy_image