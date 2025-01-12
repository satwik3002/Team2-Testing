import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# ---------- Setup and Initialization ----------
# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()  # Maximize the browser window

# Open the specified URL
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/')
time.sleep(3)

# ---------- User Registration Process ----------
# Navigate to the 'Register' page
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
time.sleep(3)

# Fill out the registration form
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
driver.find_element(By.ID, "Input_ConfirmPassword").send_keys('2003@JohnB')

# Click the 'Register' button
driver.find_element(By.ID, "registerSubmit").click()
time.sleep(3)

# ---------- User Login Process ----------
# Navigate to the 'Login' page
driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
time.sleep(3)

# Fill out the login form
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')

# Select 'Remember Me' checkbox and click 'Login'
driver.find_element(By.ID, "Input_RememberMe").click()
driver.find_element(By.ID, "login-submit").click()
time.sleep(3)

# ---------- Forgot Password Process ----------
# Navigate to the 'Forgot Password' page
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
time.sleep(3)

driver.find_element(By.XPATH, "//a[@id='forgot-password']").click()
time.sleep(3)

# Enter email for password reset
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
driver.find_element(By.XPATH, "//button[normalize-space()='Reset Password']").click()
time.sleep(3)

# ---------- Register Another User ----------
# Register as a new user
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Register')
time.sleep(3)

driver.find_element(By.ID, "Input_Email").send_keys('BBb@gmail.com')
driver.find_element(By.ID, "Input_Password").send_keys('2003@BBb')
driver.find_element(By.ID, "Input_ConfirmPassword").send_keys('2003@BBb')

# Click the 'Register' button
driver.find_element(By.ID, "registerSubmit").click()
time.sleep(3)

# ---------- Resend Email Confirmation ----------
# Navigate to 'Resend Email Confirmation' page
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
time.sleep(3)

driver.find_element(By.ID, "resend-confirmation").click()
driver.find_element(By.ID, "Input_Email").send_keys('BBb@gmail.com')
driver.find_element(By.XPATH, "//button[normalize-space()='Resend']").click()
time.sleep(3)

# ---------- Navigate to Privacy Section ----------
driver.find_element(By.XPATH, "//a[@class='nav-link text-dark'][normalize-space()='Privacy']").click()
time.sleep(3)

# ---------- Claim Creation Process ----------
# Navigate to the 'Claim' section
driver.find_element(By.XPATH, "//a[contains(text(),'Claim')]").click()
time.sleep(3)

# Create a new claim
driver.find_element(By.XPATH, "//a[contains(text(),'Create New')]").click()
driver.find_element(By.ID, "ClaimNo").send_keys('CLC1234564')
time.sleep(3)

# Select Claim Date
claim_date = driver.find_element(By.ID, "ClaimDate")
ActionChains(driver).move_to_element_with_offset(claim_date, 10, 0).click().perform()
claim_date.send_keys('12-31-2024')
time.sleep(2)

# Select Incident Date
incident_date = driver.find_element(By.ID, "IncidentDate")
ActionChains(driver).move_to_element_with_offset(incident_date, 10, 0).click().perform()
incident_date.send_keys('12-12-2024')
time.sleep(2)

# Fill out other claim details
driver.find_element(By.ID, "IncidentLocation").send_keys('HYD')
driver.find_element(By.ID, "IncidentDescription").send_keys('Rear-end collision at a traffic signal involving a private car and a truck')
driver.find_element(By.ID, "ClaimAmount").clear()
driver.find_element(By.ID, "ClaimAmount").send_keys('25000')
driver.find_element(By.ID, "SurveyorName").send_keys('Rahul Verma')
driver.find_element(By.ID, "SurveyorPhone").send_keys('9876543210')
time.sleep(2)

# Select Survey Date
survey_date = driver.find_element(By.ID, "SurveyDate")
ActionChains(driver).move_to_element_with_offset(survey_date, 10, 0).click().perform()
survey_date.send_keys('12-30-2024')
time.sleep(2)

# Add Survey Description and Claim Status
driver.find_element(By.ID, "SurveyDescription").send_keys('Detailed inspection revealed minor damage to the rear bumper and taillight')
driver.find_element(By.ID, "ClaimStatus").send_keys('S')
time.sleep(2)

# Submit the claim
driver.find_element(By.XPATH, "//input[@value='Create']").click()
time.sleep(5)

# ---------- Scroll to and Highlight the Claim ----------
claim_no = "CLC1234564"
target_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//tr[td[contains(text(), '{claim_no}')]]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_row)
driver.execute_script("arguments[0].style.border='3px solid red'", target_row)
time.sleep(2)

# ---------- Perform Actions on the Claim ----------
# Click 'Actions' button
target_row.find_element(By.XPATH, ".//button[contains(text(), 'Actions')]").click()
time.sleep(2)

# Click 'Edit' option
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit"))).click()
time.sleep(2)

# Navigate back to 'Claim' page
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Claim')
time.sleep(3)

# ---------- Delete the Claim ----------
# Scroll to and locate the claim
target_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//tr[td[contains(text(), '{claim_no}')]]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_row)
time.sleep(2)

# Click 'Actions' and 'Delete' option
target_row.find_element(By.XPATH, ".//button[contains(text(), 'Actions')]").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Delete"))).click()
time.sleep(3)

# ---------- Perform 'By Policy' Action ----------
driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Claim')
time.sleep(3)

target_row.find_element(By.XPATH, ".//button[contains(text(), 'Actions')]").click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "ByPolicy"))).click()
time.sleep(3)

# ---------- Close the Browser ----------
driver.quit()



