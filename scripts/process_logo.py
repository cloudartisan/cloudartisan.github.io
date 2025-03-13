#!/usr/bin/env python3
"""
Script to process the Blue Mountains Taekwondo logo:
1. Makes the white background transparent
2. Resizes the image to a reasonable width
3. Saves the result as a PNG with transparency
"""

import os
from PIL import Image

input_path = os.path.join('static', 'images', 'projects', 'blue-mountains-taekwondo', 'logo.png')
output_path = os.path.join('static', 'images', 'projects', 'blue-mountains-taekwondo', 'logo_small.png')

def process_logo(input_image_path, output_image_path, target_width=300):
    """
    Process the logo image to make it smaller but keep the background.
    """
    # Open the image
    img = Image.open(input_image_path)
    
    # Get the original dimensions
    width, height = img.size
    
    # Calculate new height maintaining aspect ratio
    new_height = int(height * (target_width / width))
    
    # Resize the image
    img = img.resize((target_width, new_height), Image.LANCZOS)
    
    # Save the result
    img.save(output_image_path, format='PNG')
    print(f"Processed logo saved to {output_image_path}")
    print(f"New dimensions: {target_width}x{new_height}")

if __name__ == "__main__":
    process_logo(input_path, output_path)
    print("Logo processing completed successfully.")