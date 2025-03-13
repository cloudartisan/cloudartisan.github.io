#!/usr/bin/env python3
"""
Script to crop the profile image to a circle with adjustable size and position.
This allows for precise control to remove unwanted borders.
"""

import os
import sys
from PIL import Image, ImageDraw

# Input and output paths
input_path = os.path.join('assets', 'images', 'profile_original.png')  # Original file should be renamed to this
output_path = os.path.join('assets', 'images', 'profile.png')  # Output directly to the main profile name

def create_circular_mask(input_image_path, output_image_path, scale_percent=80, offset_x=0, offset_y=0):
    """
    Create a circular image with transparency around it.
    
    Args:
        input_image_path: Path to the original image
        output_image_path: Path to save the processed image
        scale_percent: Size of the circle as a percentage of the original image (0-100)
        offset_x: Horizontal offset from center in pixels (positive moves right)
        offset_y: Vertical offset from center in pixels (positive moves down)
    """
    # Open the image
    img = Image.open(input_image_path)
    
    # Convert to RGBA if it's not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Get image dimensions
    width, height = img.size
    
    # Calculate the circle size based on scale_percent
    circle_size = int(min(width, height) * scale_percent / 100)
    
    # Create a new square image with transparency
    result = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
    
    # Create a circular mask
    mask = Image.new('L', (circle_size, circle_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, circle_size, circle_size), fill=255)
    
    # Calculate center position
    center_x = width // 2
    center_y = height // 2
    
    # Calculate crop position with offset
    left = center_x - (circle_size // 2) + offset_x
    top = center_y - (circle_size // 2) + offset_y
    right = left + circle_size
    bottom = top + circle_size
    
    # Ensure crop box is within image bounds
    left = max(0, left)
    top = max(0, top)
    right = min(width, right)
    bottom = min(height, bottom)
    
    # Adjust box size if it got clipped
    actual_width = right - left
    actual_height = bottom - top
    
    if actual_width != circle_size or actual_height != circle_size:
        print(f"Warning: Crop box was clipped. Actual size: {actual_width}x{actual_height}")
        # Adjust mask if needed
        if actual_width != circle_size or actual_height != circle_size:
            mask = mask.resize((actual_width, actual_height))
            result = Image.new('RGBA', (actual_width, actual_height), (0, 0, 0, 0))
    
    # Crop the original image
    cropped = img.crop((left, top, right, bottom))
    
    # Apply the mask to create a circular image
    result.paste(cropped, (0, 0), mask)
    
    # Save the result
    result.save(output_image_path, format='PNG')
    print(f"Circular image saved to {output_image_path}")
    print(f"Used settings: scale={scale_percent}%, offset_x={offset_x}, offset_y={offset_y}")
    
    return output_image_path

if __name__ == "__main__":
    # Default values
    scale = 70  # 70% of original size
    x_offset = 0
    y_offset = 0
    
    # Get command line arguments if provided
    if len(sys.argv) > 1:
        scale = int(sys.argv[1])
    if len(sys.argv) > 2:
        x_offset = int(sys.argv[2])
    if len(sys.argv) > 3:
        y_offset = int(sys.argv[3])
    
    print(f"Creating circular profile with scale={scale}%, x_offset={x_offset}, y_offset={y_offset}")
    create_circular_mask(input_path, output_path, scale, x_offset, y_offset)
    print("Profile image processed successfully.")