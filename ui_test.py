from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
# Uncomment this line to see the browser
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images

# Set up the Chrome WebDriver using WebDriverManager with options
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open Google and search "concepts and beyond"
    driver.get('https://www.google.com')
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds for elements to load
 
   # Take a screenshot to see the highlighted text
    driver.save_screenshot('screenshot/screenshot1_google.png')
    
    # Find the Google search box and enter the query
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("concepts and beyond")
    search_box.send_keys(u'\ue007')  # Press Enter key

     # Keep the browser open for 15 seconds
    time.sleep(2)
    
    # Take a screenshot to see the highlighted text
    driver.save_screenshot('screenshot/screenshot2_google_search_result.png')
    
     # Keep the browser open for 15 seconds
    time.sleep(1)

    # Step 2: Wait for search results and click the first one
    first_result = wait.until(EC.presence_of_element_located((By.XPATH, "(//h3)[1]/ancestor::a")))
    first_result.click()

    # Step 3: Wait for the page to fully load
    wait.until(EC.presence_of_element_located((By.XPATH, "//body")))

     # Keep the browser open for 15 seconds
    time.sleep(1)

    
    # Step 4: Search for the text "Navigating the Agile"
    text_to_find = "Navigating the Agile"
    element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text_to_find}')]")))
 
     # Keep the browser open for 15 seconds
    time.sleep(3)
    
    # Take a screenshot 
    driver.save_screenshot('screenshot/screenshot3_cnb_before.png')
    
    # Highlight the text by executing JavaScript
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)

    print("Passed: '" + text_to_find + "' text found and highlighted.")

    # Take a screenshot to verify
    driver.save_screenshot('screenshot/screenshot4_cnb_after_highlighted.png')

except (NoSuchElementException, TimeoutException):
    print("Failed: '" + text_to_find + "' text not found.")

finally:
    # Keep the browser open for 15 seconds
    time.sleep(1)
    
    # Close the browser
    driver.quit()
