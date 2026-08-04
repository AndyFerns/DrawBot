# Daily Generative Art

A small Python project that generates **one unique piece of procedural art every day**.

The artwork is deterministic: the current date is hashed into a random seed, meaning the same date will always produce the exact same image. Every new day generates a completely new composition while remaining perfectly reproducible.

<p align="center">
  <img src="art/example.png" alt="Generated artwork" width="500">
</p>

## Features

- One unique artwork per day
- Deterministic generation using the current date as the seed
- Multiple predefined color palettes
- Gradient-based backgrounds
- Distorted ("fractured") grid generation
- Random-walk line systems creating chaotic structures
- Automatically saves artwork by date

---

## How it Works

Each day, the generator performs the following steps:

1. Gets today's date (`YYYY-MM-DD`)
2. Hashes it using SHA-256
3. Converts the hash into an integer
4. Seeds Python's random number generator
5. Uses that seeded randomness to generate every artistic element

Since every random choice comes from the same seed, the artwork is completely reproducible.

For example:

| Date | Result |
|------|--------|
| `2026-08-04` | Always the same artwork |
| `2026-08-05` | A different artwork |
| `2026-08-04` (run again years later) | Identical to the original |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/daily-generative-art.git
cd daily-generative-art
```

Install dependencies:

```bash
pip install pillow
```

---

## Usage

Run the generator:

```bash
python main.py
```

The generated artwork will be saved as:

```bash
art/YYYY-MM-DD.png
```

Example:

```text
art/
├── 2026-08-01.png
├── 2026-08-02.png
├── 2026-08-03.png
└── 2026-08-04.png
```

---

## Generation Pipeline

```text
Current Date -> SHA-256 Hash -> Random Seed -> Select Palette -> Draw Gradient Background -> Generate Fractured Grid -> Generate Chaotic Walkers -> Save Artwork
```

---

## Current Art Style

Every piece currently consists of:

- A vertical gradient background
- A distorted procedural grid
- Multiple random walkers leaving interconnected paths
- A deterministic palette selected from several predefined themes

Available palettes include:

- Cosmic Scene
- Fever Dream
- Glitches in Space

---

## Roadmap

Planned improvements include:

- [ ] Procedural color palette generation using color theory
- [ ] Perlin noise backgrounds
- [ ] Bézier/spline curve systems
- [ ] Layer blending and transparency
- [ ] Animated exports
- [ ] Multiple rendering modes
- [ ] Higher-resolution rendering
- [ ] GIF generation showing the drawing process
- [ ] Command-line arguments for custom dates
- [ ] Gallery generation

---

## Why Date-Based Seeds?

Using the date as the random seed gives each day its own "identity."

Rather than generating completely arbitrary images, every day maps to a single deterministic artwork. Anyone running the generator on the same date—or regenerating a past date—will obtain the exact same result.

This creates a collection of daily artworks that are both unique and reproducible.

---

## License

This project is licensed under the MIT License.
