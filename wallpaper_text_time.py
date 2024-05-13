import os
import sys
import ctypes
import time
from PIL import Image, ImageDraw, ImageFont

# Get path to temporary directory where files are extracted
if getattr(sys, 'frozen', False):
    # Running as compiled
    app_dir = sys._MEIPASS
else:
    # Running as script
    app_dir = os.path.dirname(os.path.abspath(__file__))

# Function to create an image with text and clock
def create_wallpaper(text, font_size=200, font_path=None, image_size=(1920, 1080), text_color=(255, 255, 255), background_color=(0, 0, 0)):
    # Create a new image with the specified size and background color
    image = Image.new('RGB', image_size, color=background_color)

    # Construct full paths for font and image
    font_path = os.path.join(app_dir, "font", "distress.otf")
    image_path = os.path.join(app_dir, "wallpaper.png")

    font = ImageFont.truetype(font_path, font_size)

    # Get a drawing context
    draw = ImageDraw.Draw(image)

    # Get the bounding box of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)

    # Calculate text position
    text_x = (image_size[0] - (text_bbox[2] - text_bbox[0])) // 2
    text_y = (image_size[1] - (text_bbox[3] - text_bbox[1])) // 2

    # Draw the text on the image
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # Get current time
    current_time = time.strftime("%H:%M")

    # Get current date and day
    current_date = time.strftime("%B %d, %Y")
    current_day = time.strftime("%A")

    # Define font size and position for clock
    clock_font_size = 100
    date_font_size = 60  # Adjust this size for the date

    clock_x = 50
    clock_y = 50

    # Load fonts for clock and date
    clock_font = ImageFont.truetype(font_path, clock_font_size)
    date_font = ImageFont.truetype(font_path, date_font_size)

    # Draw clock and date on the image
    draw.text((clock_x, clock_y), current_time, fill=text_color, font=clock_font)
    draw.text((clock_x, clock_y + clock_font_size), f"{current_day}, {current_date}", fill=text_color, font=date_font)

    return image

# Function to set image as desktop wallpaper (works on Windows)
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

if __name__ == "__main__":
    # Your text to be displayed on the wallpaper
    text_to_display = "just do it"
    
    while True:
        # Generate the wallpaper image
        wallpaper_image = create_wallpaper(text_to_display)

        # Save the image to a file
        wallpaper_image.save(os.path.join(app_dir, "wallpaper.png"))

        # Set the image as desktop wallpaper
        set_wallpaper(os.path.join(app_dir, "wallpaper.png"))

        # Update every 30s
        time.sleep(30)
