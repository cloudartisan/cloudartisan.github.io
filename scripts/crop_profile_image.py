#!/usr/bin/env python3
"""
Script to crop the profile image to remove the white border.
This creates a circular profile image without a white border.
"""

import os
from PIL import Image, ImageOps

# Input and output paths
input_path = os.path.join('assets', 'images', 'profile.png')
output_path = os.path.join('assets', 'images', 'profile_cropped.png')

def crop_circular_image(input_image_path, output_image_path):
    """
    Detect the white border around the image and crop it out,
    creating a circular image with transparency around it.
    """
    # Open the image
    img = Image.open(input_image_path)
    
    # Convert to RGBA if it's not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create a circular mask
    mask = Image.new('L', img.size, 0)
    
    # Calculate the radius and center for a circular mask
    width, height = img.size
    radius = min(width, height) // 2 - 10  # Subtract 10 pixels to avoid any border
    center = (width // 2, height // 2)
    
    # Create a circular mask
    for y in range(height):
        for x in range(width):
            # Distance from center
            dist = ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5
            # If within circle, set to white
            if dist <= radius:
                mask.putpixel((x, y), 255)
    
    # Apply the mask to create a circular image
    result = Image.new('RGBA', img.size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    
    # Save the result
    result.save(output_image_path, format='PNG')
    print(f"Cropped image saved to {output_image_path}")

if __name__ == "__main__":
    crop_circular_image(input_path, output_path)
    print("Profile image processed successfully.")