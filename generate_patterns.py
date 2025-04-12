from PIL import Image, ImageDraw
import csv
import os

def create_full_black(width, height, filename):
    im = Image.new('RGB', (width, height), color="black")
    im.save(filename)

def create_full_white(width, height, filename):
    im = Image.new('RGB', (width, height), color="white")
    im.save(filename)

def create_vertical_split(width, height, filename):
    im = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(im)
    # Left half black, right half white
    draw.rectangle([0, 0, width // 2, height], fill="black")
    draw.rectangle([width // 2, 0, width, height], fill="white")
    im.save(filename)

def create_horizontal_split(width, height, filename):
    im = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(im)
    # Top half black, bottom half white
    draw.rectangle([0, 0, width, height // 2], fill="black")
    draw.rectangle([0, height // 2, width, height], fill="white")
    im.save(filename)

def create_checkerboard(width, height, filename, box_size=50):
    im = Image.new('RGB', (width, height), color="white")
    draw = ImageDraw.Draw(im)
    # Create alternating black and white squares
    num_cols = width // box_size
    num_rows = height // box_size
    for row in range(num_rows):
        for col in range(num_cols):
            if (row + col) % 2 == 0:
                top_left = (col * box_size, row * box_size)
                bottom_right = ((col + 1) * box_size, (row + 1) * box_size)
                draw.rectangle([top_left, bottom_right], fill="black")
    im.save(filename)

def create_black_circle_on_white(width, height, filename):
    im = Image.new('RGB', (width, height), color="white")
    draw = ImageDraw.Draw(im)
    # Draw a black circle in the center
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    draw.ellipse([center[0] - radius, center[1] - radius,
                  center[0] + radius, center[1] + radius], fill="black")
    im.save(filename)

def create_white_square_on_black(width, height, filename):
    im = Image.new('RGB', (width, height), color="black")
    draw = ImageDraw.Draw(im)
    # Draw a white square in the center
    square_size = min(width, height) // 2
    top_left = ((width - square_size) // 2, (height - square_size) // 2)
    bottom_right = (top_left[0] + square_size, top_left[1] + square_size)
    draw.rectangle([top_left, bottom_right], fill="white")
    im.save(filename)

def main():
    # Set the image resolution
    width = 1920
    height = 1080

    # Create output directory if it doesn't exist
    output_dir = "patterns"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    catalog = []  # list to hold (Pattern ID, Description, Filename)
    
    # Define all pattern-generating functions with a unique ID and description
    patterns = [
        ("Pattern_A_FullBlack", "Full Black Screen", create_full_black),
        ("Pattern_B_FullWhite", "Full White Screen", create_full_white),
        ("Pattern_C_VerticalSplit", "Vertical Split: Left Black, Right White", create_vertical_split),
        ("Pattern_D_HorizontalSplit", "Horizontal Split: Top Black, Bottom White", create_horizontal_split),
        ("Pattern_E_Checkerboard", "Checkerboard Pattern", create_checkerboard),
        ("Pattern_F_BlackCircleOnWhite", "Black Circle on White Background", create_black_circle_on_white),
        ("Pattern_G_WhiteSquareOnBlack", "White Square on Black Background", create_white_square_on_black)
    ]
    
    # Generate each pattern image and add its details to the catalog
    for pattern_id, description, func in patterns:
        filename = os.path.join(output_dir, pattern_id + ".png")
        # For the checkerboard, adjust the box size if desired (here we use 100)
        if pattern_id == "Pattern_E_Checkerboard":
            func(width, height, filename, box_size=100)
        else:
            func(width, height, filename)
        catalog.append((pattern_id, description, filename))
        print(f"Generated {filename}")
        
    # Write a CSV catalog for the generated patterns
    with open("pattern_catalog.csv", mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Pattern ID", "Description", "Filename"])
        for row in catalog:
            writer.writerow(row)
    print("Catalog saved as pattern_catalog.csv")

if __name__ == "__main__":
    main()
