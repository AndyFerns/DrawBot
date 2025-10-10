import datetime
import random
import hashlib
import os
from PIL import Image, ImageDraw

# config
WIDTH = 1080
HEIGHT = 1080
ART_DIR = "art"

PALETTES = [
    {
        "name": "Cosmic Scene",
        "bg_start": (0, 0, 10),
        "bg_end": (5, 0, 25),
        "lines": [(255, 255, 255), (100, 100, 255)],
        "grid": (40, 40, 80),
    },
    {
        "name": "Fever Dream",
        "bg_start": (20, 5, 5),
        "bg_end": (50, 10, 10),
        "lines": [(255, 220, 180), (255, 100, 100)],
        "grid": (100, 60, 60),
    },
    {
        "name": "Glitches in Space",
        "bg_start": (15, 25, 15),
        "bg_end": (0, 10, 0),
        "lines": [(200, 255, 200), (150, 255, 250)],
        "grid": (50, 90, 50),
    },
]


def generate_seeded_art():
    """
    generates a unique piece of art utilizing the seed as the current date
    """
    date_str = datetime.date.today().isoformat()
    # convert the date string into a consistent seed number
    seed_hash = hashlib.sha256(date_str.encode()).hexdigest()
    seed = int(seed_hash, 16)
    random.seed(seed)

    print(f"Generating art for {date_str} with seed {seed}")

    # base image values
    bg_color = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
    img = Image.new('RGB', (WIDTH, HEIGHT), color=bg_color)
    draw = ImageDraw.Draw(img, 'RGBA') # RGBA for transparency

    num_circles = random.randint(50, 150)

    for _ in range(num_circles):
        # Random position
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        
        # Random radius
        radius = random.randint(50, 300)
        
        # Random color with transparency (Alpha channel)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        alpha = random.randint(50, 100) # Semi-transparent
        color = (r, g, b, alpha)
        
        # Draw the circle (as an ellipse with the same width and height)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)

    # Ensure the 'art' directory exists
    os.makedirs(ART_DIR, exist_ok=True)
    
    file_path = os.path.join(ART_DIR, f"{date_str}.png")
    img.save(file_path)
    print(f"✅ Art saved successfully to {file_path}")


if __name__ == '__main__':
    generate_seeded_art()