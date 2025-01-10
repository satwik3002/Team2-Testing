import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/')
driver.maximize_window()
time.sleep(3)

# Login Process
Login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
Login.click()
time.sleep(2)

# Input email and password
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
time.sleep(2)
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
time.sleep(2)
driver.find_element(By.ID, "Input_RememberMe").click()
time.sleep(2)
SubmitButton = driver.find_element(By.ID, "login-submit")
SubmitButton.click()
time.sleep(2)

# Navigate to Products section
ProductButton = driver.find_element(By.XPATH, "//a[normalize-space()='Product']")
ProductButton.click()
time.sleep(3)

# Create a new product
driver.find_element(By.XPATH, "//a[normalize-space()='Create New']").click()
time.sleep(3)

# Input product details
driver.find_element(By.ID, "ProductID").send_keys('PROD201112')
time.sleep(3)
driver.find_element(By.ID, "ProductName").send_keys('Comprehensive Car Plan')
time.sleep(3)
driver.find_element(By.ID, "ProductDescription").send_keys('Full coverage for personal cars')
time.sleep(3)
driver.find_element(By.ID, "ProductUIN").send_keys('UINCAR12345698756456')
time.sleep(3)
driver.find_element(By.ID, "InsuredInterests").send_keys('private car')
time.sleep(3)
driver.find_element(By.ID, "PolicyCoverage").send_keys('Collision, Theft, Natural Calamities')
time.sleep(3)

# Submit the product creation form
driver.find_element(By.CSS_SELECTOR, "input[value='Create']").click()
time.sleep(6)

# Wait for the product table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table"))
)

# Define the Product ID to search for
product_id = "PROD201112"

# Locate the row with the product ID
target_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]"))
)

# Scroll to the row containing the product ID
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_row)

# Wait for the "Actions" button and click it
actions_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]//button[contains(text(), 'Actions')]"))
)
actions_button.click()
time.sleep(5)

# Perform Edit action
edit_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Edit"))
)
edit_option.click()
time.sleep(3)

# Modify Insured Interests field
driver.find_element(By.XPATH, "//input[@id='InsuredInterests']").clear()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='InsuredInterests']").send_keys('public car')
time.sleep(3)
driver.find_element(By.XPATH, "//input[@value='Save']").click()
time.sleep(5)

# Navigate back to the Product section
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Product')
time.sleep(3)

# Wait for the table to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table"))
)

# Scroll to the product ID and click on "Actions" again
target_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_row)
actions_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]//button[contains(text(), 'Actions')]"))
)
actions_button.click()
time.sleep(5)

# Perform Details action
Details_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Details"))
)
Details_option.click()
time.sleep(3)

# Navigate back to the Product section
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Product')
time.sleep(3)

# Scroll to the product and perform Delete action
target_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_row)
actions_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]//button[contains(text(), 'Actions')]"))
)
actions_button.click()
time.sleep(5)

Delete_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Delete"))
)
Delete_option.click()
time.sleep(3)

# Navigate back to the Product section
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Product')
time.sleep(3)

# Scroll and perform Add-on action
scroll_position = 1579
driver.execute_script(f"window.scrollTo(0, {scroll_position});")
actions_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//tr[td[contains(text(), '{product_id}')]]//button[contains(text(), 'Actions')]"))
)
actions_button.click()
time.sleep(5)

Addon_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Add-on"))
)
Addon_option.click()
time.sleep(3)

# Create a new Add-on
CreateNew = driver.find_element(By.XPATH, "//a[normalize-space()='Create New']")
CreateNew.click()
time.sleep(3)

#Handle Product ID Dropdown using JavaScript to avoid visibility issues
dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ProductID")))
dropdown.click()  # Click to expand the dropdown
time.sleep(2)

#Use JavaScript to select the option "PROD201113"
driver.execute_script("document.querySelector('#ProductID').value='PROD201112';")
time.sleep(2)


# Input Add-on details
driver.find_element(By.ID, "AddonID").send_keys('A001234567')
time.sleep(2)
driver.find_element(By.ID, "AddonTitle").send_keys('Premium Support')
time.sleep(2)
driver.find_element(By.ID, "AddonDescription").send_keys('Provides 24/7 priority customer support.')
time.sleep(2)
Create = driver.find_element(By.XPATH, "//input[@value='Create']")
Create.click()
time.sleep(5)

# Open the ProductAddon page
addon_page_url = 'https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/ProductAddon?productId=PROD201112'
driver.get(addon_page_url)
time.sleep(3)

# Add-On ID
addon_id = 'PROD201112'

# Function to perform actions on the Add-on row
def perform_action(option_text):
    try:
        # Re-locate the row containing the specified Add-On ID
        row_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//tr[td[contains(text(), '{addon_id}')]]"))
        )

        # Scroll to the specific row
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", row_element)

        # Click the "Actions" button within the row
        action_button_element = row_element.find_element(By.XPATH, ".//button[contains(text(), 'Actions')]")
        action_button_element.click()
        time.sleep(2)

        # Click the desired option from the dropdown
        option_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, option_text))
        )
        option_element.click()
        time.sleep(3)
    except Exception as e:
        print(f"Error performing {option_text}: {e}")

# Perform actions on the Add-on (Edit, Details, Delete)
perform_action('Edit')
driver.find_element(By.ID,"AddonDescription").clear()
time.sleep(3)
driver.find_element(By.ID,"AddonDescription").send_keys('Covers emergency roadside services')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='Save']").click()
time.sleep(3)
driver.get(addon_page_url)
time.sleep(3)

perform_action('Details')
driver.get(addon_page_url)
time.sleep(3)
perform_action('Delete')

# Navigate back to the Add-on page
driver.get(addon_page_url)
time.sleep(3)

# Close the browser after all actions
driver.quit()


