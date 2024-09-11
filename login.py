import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_driver_path = r"C:\Program Files (x86)\Google\chromedriver-win64\chromedriver.exe"

# Using undetected_chromedriver for Google login
def google_login(email, password):
    service = Service(executable_path=chrome_driver_path)
    driver = uc.Chrome(service=service)  # Pass the service with the specified path
    
    driver.get("https://www.chess.com")
    
    # Wait for the email input field to be present and interactable
    wait = WebDriverWait(driver, 20)
    
    # Click on the login button on chess.com homepage
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/"]')))
    login_button.click()
    print("Navigated to the login page.")  

    # Click on "Log in with Google"
    google_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://www.chess.com/login/google"]')))
    google_login_button.click()
    print("Clicked 'Log in with Google'.")

    try:
        # Wait for the email input field to be visible
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        print("Entered email.")
    except Exception as e:
        print(f"Error finding email input: {e}")
        driver.quit()
        return None
    
    # Wait for password input to be available and enter password
    try:
        time.sleep(2)
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        print("Entered password.")
    except Exception as e:
        print(f"Error finding password input: {e}")
        driver.quit()
        return None
    
    # Handle Google confirmation page (if needed)
    try:
        time.sleep(5)
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@jsname="LgbsSe"]')))
        continue_button.click()
        print("Clicked on 'Continue' button.")
    except Exception:
        print("No 'Continue' button found, possible skipping.")

    return driver

if __name__ == "__main__":
    # Google account credentials
    email = "your_email"  
    password = "your password"     

    # Log in to Google using undetected_chromedriver
    google_driver = google_login(email, password)
    
    time.sleep(5)
    print("Chess.com login successful.")
    google_driver.quit()

