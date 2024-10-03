import boto3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize AWS Device Farm client and create TestGrid URL
devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
testgrid_url_response = devicefarm_client.create_test_grid_url(
    projectArn="arn:aws:devicefarm:us-west-2:<your_project_arn>",  # Replace with your actual project ARN
    expiresInSeconds=300  # URL will be valid for 5 minutes
)

# Set up the Remote WebDriver to connect to the AWS Device Farm TestGrid
driver = webdriver.Remote(
    command_executor=testgrid_url_response["url"],
    desired_capabilities=webdriver.DesiredCapabilities.FIREFOX
)

try:
    driver.implicitly_wait(30)
    driver.maximize_window()

    # Step 1: Open Google and search "concepts and beyond"
    driver.get("https://www.google.com")
    
    # Wait for the search box and enter the query
    search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("concepts and beyond")
    search_box.send_keys(Keys.RETURN)

    # Screenshot of the search results
    driver.save_screenshot('screenshot/screenshot1_google.png')

    # Step 2: Check if an element is found after the window is maximized
    if driver.find_element(By.ID, "Layer_1"):
        print("Graphics generated in full screen")

    assert driver.find_element(By.ID, "Layer_1")

    # Step 3: Resize the window and reload the URL
    driver.set_window_position(0, 0)
    driver.set_window_size(1000, 400)
    driver.get("<sample_url>")  # Replace with the desired URL

    # Step 4: Check if graphics appear after resizing the window
    tower = driver.find_element(By.ID, "Layer_1")
    if tower.is_displayed():
        print("Graphics generated after resizing")
    else:
        print("Graphics not generated at this window size")
        # Raise an error to fail the script if expected graphics do not load
        raise Exception("Expected graphics not generated after resizing")

except NoSuchElementException as e:
    print(f"Element not found: {e}")
except TimeoutException as e:
    print(f"Timeout occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
