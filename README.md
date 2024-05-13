# Wallpaper Text Time

This Python script allows you to create a custom wallpaper with text and a clock display, and set it as your desktop background. It's especially useful for displaying motivational quotes or reminders along with the current time and date.

## Features

- **Custom Text:** You can specify the text you want to display on the wallpaper.
- **Customizable Fonts:** You can choose the font size and style for both the main text and the clock/date display.
- **Automatic Update:** The wallpaper updates automatically at regular intervals (default: every 30 seconds), ensuring that the time displayed is always accurate.
- **Windows Compatibility:** The script is compatible with Windows and uses ctypes to set the wallpaper.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

## Usage

1. Ensure you have Python installed on your system.
2. Install the required PIL library by running `pip install pillow`.
3. Clone or download this repository to your local machine.
4. Customize the script:
   - Optionally, change the `text_to_display` variable in the `__main__` block to your desired text.
   - Adjust the font size, font path, text color, background color, etc., as needed in the `create_wallpaper()` function.
5. Run the script:
   - If you want to run it in the console, execute `python wallpaper_text_time.py`.
   - If you want to run it as a background process without a console window, execute `pythonw wallpaper_text_time.pyw`.
6. Your wallpaper will be updated with the specified text and clock display. Enjoy your personalized wallpaper!

## Note

- This script is designed to run on Windows systems due to its dependency on ctypes for setting the wallpaper. It may require modifications to work on other operating systems.
