#!/usr/bin/env python3
"""
Script to crop the profile image to remove the white border.
This creates a circular profile image without a white border.
"""

import os
from PIL import Image, ImageDraw

# Input and output paths
input_path = os.path.join('assets', 'images', 'profile.png')
output_path = os.path.join('assets', 'images', 'profile_cropped.png')

def create_circular_mask(input_image_path, output_image_path):
    """
    Create a perfectly circular image with transparency around it.
    """
    # Open the image
    img = Image.open(input_image_path)
    
    # Convert to RGBA if it's not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Get image dimensions
    width, height = img.size
    size = min(width, height)
    
    # Create a new square image with transparency
    result = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    
    # Create a circular mask
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    # Calculate offset to center the original image
    offset_x = (width - size) // 2
    offset_y = (height - size) // 2
    
    # Crop the original image to a square
    cropped = img.crop((offset_x, offset_y, offset_x + size, offset_y + size))
    
    # Apply the mask to create a circular image
    result.paste(cropped, (0, 0), mask)
    
    # Save the result
    result.save(output_image_path, format='PNG')
    print(f"Circular image saved to {output_image_path}")

if __name__ == "__main__":
    create_circular_mask(input_path, output_path)
    print("Profile image processed successfully.")