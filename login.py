from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set up ChromeDriver service
service = Service(executable_path=r"C:\Program Files (x86)\Google\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open chess.com
driver.get("https://www.chess.com/")
wait = WebDriverWait(driver, 10)

# Click on the login button on chess.com homepage
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/"]')))
login_button.click()
print("Navigated to the login page.")

# Click on "Log in with Google"
google_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://www.chess.com/login/google"]')))
google_login_button.click()
print("Clicked 'Log in with Google'.")

# Switch to Google login page and enter email
wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
email_input = driver.find_element(By.NAME, "identifier")
email_input.send_keys("madiyar03633@gmail.com")
email_input.send_keys(Keys.RETURN)
print("Entered email.")

# Wait for password input and enter password
time.sleep(2)
password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
password_input.send_keys("zz05052004")
password_input.send_keys(Keys.RETURN)
print("Entered password.")

# Handle Google confirmation page (if needed)
time.sllep(5)
try:
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@jsname="LgbsSe"]')))
    continue_button.click()
    print("Clicked on 'Continue' button.")
except:
    print("No 'Continue' button found, possible skipping.")


# Wait for chess.com load
time.sleep(5)
print("Logged into chess.com succesfully.")

driver.quit()