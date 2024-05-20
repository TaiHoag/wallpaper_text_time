# Wallpaper Text Time

This Python script allows you to create a custom wallpaper with text and a clock display, and set it as your desktop background. It's especially useful for displaying motivational quotes or reminders along with the current time and date.

## Features

- **Custom Text:** You can specify the text you want to display on the wallpaper.
- **Customizable Fonts:** You can choose the font size and style for both the main text and the clock/date display.
- **Automatic Update:** The wallpaper updates automatically at regular intervals (default: every 30 seconds), ensuring that the time displayed is always accurate.
- **Windows Compatibility:** The script is compatible with Windows and uses ctypes to set the wallpaper.

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) library for image manipulation
- `ctypes` library (part of the Python standard library)
- A valid .otf font file

## Usage

1. Ensure you have Python installed on your system.
2. Install the required PIL library by running `pip install pillow`.
3. Clone or download this repository to your local machine.
4. Customize the script:
   - Optionally, change the `text_to_display` variable in the `__main__` block to your desired text (only in .py, for .pyw, update the `config.json`).
   - Adjust the font size, font path, text color, background color, etc., as needed in the `create_wallpaper()` function.
5. Run the script:
   - If you want to run it in the console, execute `python wallpaper_text_time.py`.
   - If you want to run it as a background process without a console window, execute `pythonw wallpaper_text_time.pyw`.
6. Your wallpaper will be updated with the specified text and clock display. Enjoy your personalized wallpaper!

## Usage on Windows Startup

You can configure the script to run automatically when your Windows system starts up by creating a shortcut to the compiled executable file (.exe) and placing it in the Startup folder. Here's how to do it:

1. **Compile the Script:**
   - Use PyInstaller to convert the Python script (`wallpaper_text_time.pyw`) into a standalone executable (.exe) file.
   - Run the following command in the terminal:
     ```
     pyinstaller --onefile --add-data "distress.otf;." --add-data "wallpaper.png;." --add-data "config.json;." wallpaper_text_time.pyw
     ```
   - This will create a `dist` directory containing the compiled executable file (`wallpaper_text_time.exe`).

2. **Create Shortcut:**
   - Navigate to the `dist` directory where the compiled executable is located.
   - Right-click on `wallpaper_text_time.exe` and select "Create shortcut".
   - Move the shortcut to a location where it will be easily accessible, such as the desktop.

3. **Access Startup Folder:**
   - Press `Win + R` to open the "Run" dialog box.
   - Type `shell:startup` and press Enter. This will open the Startup folder.

4. **Add Shortcut to Startup:**
   - Copy the shortcut (`wallpaper_text_time.exe`) that you created earlier.
   - Paste the shortcut into the Startup folder.
   - The script will now run automatically each time you start your Windows system.

Now, whenever you boot up your Windows computer, the script will automatically run in the background, updating your desktop wallpaper with the custom text and clock display.

## Configuration

Edit the `config.json` file to customize the wallpaper. Here is an example configuration:

```json
{
    "text": "just do it",
    "font_size": 200,
    "font_path": "distress.otf",
    "image_size": [1920, 1080],
    "text_color": [255, 255, 255],
    "background_color": [0, 0, 0],
    "clock_font_size": 100,
    "date_font_size": 60,
    "clock_position": [50, 50]
}
```

## Note

-  Ensure that the Python environment and required libraries are available on your system for the script to execute successfully.
-  If you wan to test or install new config, remember to end task (Using Task Manager) of the on-going scripts (for .pyw) or `ctrl + C` in the terminal (for .py)
