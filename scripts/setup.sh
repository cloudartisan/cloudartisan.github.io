#!/bin/bash
# Setup script for movie data automation

echo "Setting up movie data automation..."

# Check if pip is available
if command -v pip3 &> /dev/null; then
    echo "Installing Python dependencies..."
    pip3 install -r requirements.txt
elif command -v pip &> /dev/null; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
else
    echo "Error: pip not found. Please install Python dependencies manually:"
    echo "pip install requests PyYAML beautifulsoup4 lxml"
    exit 1
fi

echo "Setup complete!"
echo ""
echo "Usage:"
echo "  ./update_movie_data.py    # Update all movie data"
echo "  hugo                      # Rebuild site with updated data"