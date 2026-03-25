"""
Remove white background from buaa.png, keeping only the blue content.
Output: assets/files/institute/buaa_transparent.png
"""
from PIL import Image

INPUT = "assets/files/institute/buaa.png"
OUTPUT = "assets/files/institute/buaa_transparent.png"
THRESHOLD = 240  # pixels with R,G,B all >= this are treated as white


def remove_white(input_path, output_path, threshold=THRESHOLD):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if r >= threshold and g >= threshold and b >= threshold:
                pixels[x, y] = (r, g, b, 0)  # fully transparent
    img.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    remove_white(INPUT, OUTPUT)
