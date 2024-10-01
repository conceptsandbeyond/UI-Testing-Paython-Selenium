# Setting Up Selenium Testing Code on Windows

This guide provides step-by-step instructions to set up and run your Selenium testing code on a local Windows environment.

## Prerequisites

- Python installed (preferably Python 3.x)
- Basic knowledge of Python and Selenium
- Google Chrome browser installed
- ChromeDriver corresponding to your Chrome version
- The Selenium testing code

## Step 1: Install Python

1. **Download Python**:
   - Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python.

2. **Install Python**:
   - Run the installer and make sure to check the box that says "Add Python to PATH."
   - Complete the installation by following the prompts.

3. **Verify Installation**:
   Open a command prompt and run:
   ```bash
   python --version
   ```

## Step 2: Install Selenium

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and hit Enter
2. **Install Selenium using Pip**:
   - In the command prompt, run:
   ```bash
   pip install selenium
   ```

## Step 3: Download ChromeDriver

1. **Check Chrome Version**:
   - Open Google Chrome.
   - Click on the three-dot menu in the top right corner > Help > About Google Chrome.
   - Note the version number (e.g., 93.0.4577.63).
     
2. **Download ChromeDriver**:

   - Go to the ChromeDriver download page.
   - Download the version that matches your Chrome version.
   - Extract the downloaded file (e.g., chromedriver.exe).
   
3. **Add ChromeDriver to PATH**:

   - Move chromedriver.exe to a folder of your choice (e.g., C:\chromedriver).
   - Add this folder to your system PATH:
     - Right-click on `This PC` or `Computer` and select `Properties`.
       - Click on "Advanced system settings."
       - Click on the "Environment Variables" button.
       - In the "System variables" section, find the "Path" variable and select it.
       - Click "Edit," then "New," and add the path to the folder containing chromedriver.exe.
       - Click "OK" to close all dialog boxes.
     
## Step 4: Check Your Selenium Test Script ##

1. Open your selenium script `ui_test.py` file.

## Step 5: Run Your Selenium Test ##
1. **Open Command Prompt**: Press `Win + R`, type cmd, and hit Enter.

2. **Navigate to Your Script's Directory**: Use the cd command to navigate to the directory where your `ui_test.py` file is located:
    
    ```bash
    cd path_to_your_script_directory
    ```
3. **Run Your Script**: In the command prompt, 
run:
    ```bash
    python ui_test.py
   ```

### Conclusion ###
This guide provides the steps to set up and run your Selenium tests on a local Windows environment. If you encounter any issues or have questions, feel free to seek help or consult the official Selenium documentation.


### How to Use
1. Create a new file named `README.md` in your project directory.
2. Copy and paste the above content into that file.
3. Save the file.

This `README.md` file will serve as a comprehensive guide for anyone looking to set up and run Selenium testing code on a local Windows environment. If you need any modifications or additional information, let me know!






