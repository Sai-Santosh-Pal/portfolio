import os
from rembg import remove
from PIL import Image
import io

# Path to your assets directory
ASSETS_DIR = "./assets"

# Ensure output keeps transparency
def remove_background(input_path, output_path):
    with open(input_path, "rb") as i:
        input_bytes = i.read()
        output_bytes = remove(input_bytes)
        img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
        img.save(output_path)

# Process all files starting with 'red_'
for filename in os.listdir(ASSETS_DIR):
    filepath = os.path.join(ASSETS_DIR, filename)
    output_path = filepath  # Overwrite original
    remove_background(filepath, output_path)
        
