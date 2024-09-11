# Chess.com Google Login Automation

This Python script automates the login process to **Chess.com** using **Google** authentication. It leverages **Selenium** and **undetected-chromedriver** to handle the login steps and bypass Google’s bot detection, ensuring smooth access to Chess.com through a Google account.

## Features

- Automates the process of logging into Chess.com using Google credentials.
- Uses **undetected-chromedriver** to bypass Google's automated bot detection.
- Waits for elements to load using **WebDriverWait** for better interaction with dynamic pages.
- Handles email and password entry for Google authentication.

## Installation

1. **Download ChromeDriver**:
    Make sure to download the correct version of ![ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=ru) that matches your Google Chrome browser version.

2. **Install the required dependencies**:
    Run the following command to install selenium and undetected-chromedriver:
    ```
    pip install selenium undetected-chromedriver
    ```

## Usage
1. **Wait for the script to finish**:
    The script will:
    - Open chess.com and navigate to the login page.
    - Select the **Login with Google** option.
    - Enter your email and password for Google.
    - Log into chess.com
