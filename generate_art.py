import datetime
import random
import hashlib
import os
import math
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

def draw_gradient_background(draw, width, height, start_color, end_color):
    """
    Draws a vertical gradient representing the 'void'.
    """
    for y in range(height):
        # Interpolate color
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (y / height))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (y / height))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_chaotic_walkers(draw, width, height, palette):
    """
    Draws frenetic lines using a random walk algorithm.
    """
    num_walkers = random.randint(3, 8)
    for _ in range(num_walkers):
        x, y = random.uniform(0, width), random.uniform(0, height)
        steps = random.randint(200, 500)
        color = random.choice(palette["lines"])
        for _ in range(steps):
            px, py = x, y
            angle = random.uniform(0, 2 * math.pi)
            step_size = random.uniform(5, 25)
            x += math.cos(angle) * step_size
            y += math.sin(angle) * step_size
            
            # Keep walkers on screen
            x = max(0, min(width - 1, x))
            y = max(0, min(height - 1, y))

            draw.line([(px, py), (x, y)], fill=color, width=1)

def draw_fractured_grid(draw, width, height, palette):
    """
    Draws a distorted grid, representing fragile order.
    """
    step = random.randint(50, 150)
    jolt = step / 4
    
    points = []
    for x in range(0, width + step, step):
        col = []
        for y in range(0, height + step, step):
            nx = x + random.uniform(-jolt, jolt)
            ny = y + random.uniform(-jolt, jolt)
            col.append((nx, ny))
        points.append(col)

    # Draw lines
    for i in range(len(points)):
        for j in range(len(points[i])):
            if i + 1 < len(points):
                draw.line([points[i][j], points[i+1][j]], fill=palette["grid"], width=1)
            if j + 1 < len(points[i]):
                draw.line([points[i][j], points[i][j+1]], fill=palette["grid"], width=1)


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