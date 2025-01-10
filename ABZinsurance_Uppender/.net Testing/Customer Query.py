import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/')
driver.maximize_window()  # Maximize the browser window
time.sleep(3)  # Wait for the page to load

# Navigate to the 'Register' page
Register = driver.find_element(By.XPATH, "//a[normalize-space()='Register']")
Register.click()
time.sleep(3)  # Wait for the register page to load

# Fill out the registration form
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
time.sleep(2)
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
time.sleep(2)
driver.find_element(By.ID, "Input_ConfirmPassword").send_keys('2003@JohnB')
time.sleep(2)
ClickRegister = driver.find_element(By.ID, "registerSubmit")
ClickRegister.click()
time.sleep(2)

# Navigate to the login page
Login = driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
Login.click()
time.sleep(2)

# Fill out the login form
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
time.sleep(2)
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
time.sleep(2)
driver.find_element(By.ID, "Input_RememberMe").click()
time.sleep(2)
SubmitButton = driver.find_element(By.ID, "login-submit")
SubmitButton.click()
time.sleep(2)

# Navigate to the 'Forgot Password' page
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
time.sleep(3)

ForgetPassword = driver.find_element(By.XPATH, "//a[@id='forgot-password']")
ForgetPassword.click()
time.sleep(3)
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
time.sleep(3)
ResetPassword = driver.find_element(By.XPATH, "//button[normalize-space()='Reset Password']")
ResetPassword.click()
time.sleep(3)

# Navigate back to the login page
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
time.sleep(3)

# Register as a new user
RegisterAsNewUser = driver.find_element(By.XPATH, "//a[normalize-space()='Register as a new user']")
RegisterAsNewUser.click()
driver.find_element(By.ID, "Input_Email").send_keys('BBb@gmail.com')
time.sleep(2)
driver.find_element(By.ID, "Input_Password").send_keys('2003@BBb')
time.sleep(2)
driver.find_element(By.ID, "Input_ConfirmPassword").send_keys('2003@BBb')
time.sleep(2)
ClickRegister = driver.find_element(By.ID, "registerSubmit")
ClickRegister.click()
time.sleep(2)

# Navigate to the 'Resend Email' option for verification
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
time.sleep(3)

ResendEmail = driver.find_element(By.ID, "resend-confirmation")
ResendEmail.click()
time.sleep(3)
driver.find_element(By.ID, "Input_Email").send_keys('BBb@gmail.com')
time.sleep(3)
ReSendButton = driver.find_element(By.XPATH, "//button[normalize-space()='Resend']")
ReSendButton.click()
time.sleep(2)
#Checking the title
actual_title = driver.title
expect_title = "Home Page - ABZVehicleInsuranceMvcProject"

driver.save_screenshot(".//actual_title.png")
print(driver.title)
if actual_title == expect_title:
    print("Home page open Successfully")
else:
    print("Unsuccessful")

#Navigate to the'Customer Query'
CustomerQuery=driver.find_element(By.XPATH,"//a[normalize-space()='CustomerQuery']").click()
Create=driver.find_element(By.XPATH,"//a[normalize-space()='Create New']")
Create.click()
# Fill query form
query_id_input = driver.find_element(By.ID, "QueryID")
query_id_input.send_keys("1234567890")

customer_id_input = driver.find_element(By.ID, "CustomerID")
customer_id_input.send_keys("1234567890")

description_input = driver.find_element(By.ID, "Description")
description_input.send_keys("Test Query")

query_date_input = driver.find_element(By.ID, "QueryDate")
query_date_input.send_keys("10-02-2024")

status_input = driver.find_element(By.ID, "Status")
status_input.send_keys("Pending")

# Click on Submit button
actions = ActionChains(driver)
create_button = driver.find_element(By.XPATH, "//input[@value='Create']")
actions.move_to_element(create_button).click().perform()
time.sleep(3)
# Close the browser
driver.quit()
