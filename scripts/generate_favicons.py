#!/usr/bin/env python3
"""
Script to generate favicon files from the profile image.
"""

import os
from PIL import Image

def generate_favicons(source_image, output_dir):
    """
    Generate various favicon sizes from source image.
    """
    # Open the source image
    img = Image.open(source_image)
    
    # Ensure it's square
    width, height = img.size
    size = min(width, height)
    
    # Crop to square from center
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size
    img = img.crop((left, top, right, bottom))
    
    # Generate favicon.ico (16x16, 32x32, 48x48)
    favicon_sizes = [16, 32, 48]
    favicon_images = []
    
    for size in favicon_sizes:
        favicon_images.append(img.resize((size, size), Image.LANCZOS))
    
    favicon_path = os.path.join(output_dir, "favicon.ico")
    favicon_images[0].save(
        favicon_path,
        format="ICO", 
        sizes=[(size, size) for size in favicon_sizes],
        append_images=favicon_images[1:]
    )
    print(f"Created {favicon_path}")
    
    # Generate individual PNG files
    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512
    }
    
    for filename, size in sizes.items():
        output_path = os.path.join(output_dir, filename)
        img.resize((size, size), Image.LANCZOS).save(output_path, format="PNG")
        print(f"Created {output_path}")
    
    # Create site.webmanifest
    manifest_path = os.path.join(output_dir, "site.webmanifest")
    manifest_content = """{
  "name": "Cloud Artisan",
  "short_name": "Cloud Artisan",
  "icons": [
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "display": "standalone"
}"""
    
    with open(manifest_path, "w") as f:
        f.write(manifest_content)
    print(f"Created {manifest_path}")

if __name__ == "__main__":
    source_image = os.path.join('assets', 'images', 'profile.png')
    output_dir = os.path.join('static')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    generate_favicons(source_image, output_dir)
    print("Favicon generation completed successfully.")