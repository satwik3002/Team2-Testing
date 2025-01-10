from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Open chrome and start the link
driver = webdriver.Chrome()
URL = "https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/"
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL)

# Checking the title
actual_title = driver.title
expected_title = "Home Page - ABZVehicleInsuranceMvcProject"
driver.save_screenshot(".//actual_title.png")
print(driver.title)
if actual_title == expected_title:
    print("Home page open Successfully")
else:
    print("Unsuccessful")

# Click on login button
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(1)

#Click on login button
# Click on Login
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(1)

# Fill login form
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
driver.find_element(By.ID, "login-submit").click()
time.sleep(10)
#navigating Query response
QueryResponse=driver.find_element(By.XPATH,"//a[normalize-space()='QueryResponse']").click()
Create=driver.find_element(By.XPATH,"//a[normalize-space()='Create New']")
Create.click()

# Fill query form
query_id_input = driver.find_element(By.ID, "QueryID")
query_id_input.send_keys("1234567890")

sr_no_input = driver.find_element(By.ID, "SrNo")
sr_no_input.send_keys("1234567890")

agent_id_input = driver.find_element(By.ID, "AgentID")
agent_id_input.send_keys("2345678890")

description_input = driver.find_element(By.ID, "Description")
description_input.send_keys("Test Query")

response_date_input = driver.find_element(By.ID, "ResponseDate")
response_date_input.send_keys("10-02-2024")

# Click on Submit button
actions = ActionChains(driver)
create_button = driver.find_element(By.XPATH, "//input[@value='Create']")
actions.move_to_element(create_button).click().perform()
# Wait for 5 seconds
time.sleep(5)


#Scroll to the required position to find the claim number
scroll_position = 1579


# Perform actions on the row, such as clicking the "Actions" button
actions_button = driver.find_element(By.XPATH, ".//button[contains(text(), 'Actions')]")
actions_button.click()
time.sleep(3)

# Click the 'Edit' option
edit_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Edit"))
)
edit_option.click()
driver.find_element(By.ID,"AgentID").send_keys("9876543210")
driver.find_element(By.XPATH,"//input[@value='Save']")
time.sleep(3)
driver.quit()
