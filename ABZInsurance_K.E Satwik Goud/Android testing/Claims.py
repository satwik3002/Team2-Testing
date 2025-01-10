from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1: Desired Capabilities
# These are the capabilities required to run the automation on an Android emulator or device
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:platformVersion": "15",  # Android version on the device/emulator
    "appium:deviceName": "emulator-5554",  # Device/emulator identifier
    "app": "D:\\TestAPK\\app-debug.apk"  # Path to the app under test
}

# Step 2: Create Driver Object
# Creating the driver to connect to the Appium server with the specified options
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(15)  # Wait for the app to load

# Step 3: Login
# Entering email and password to log in
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/email_editText").send_keys('JohnB@gmail.com')
time.sleep(3)
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/password_editText").send_keys('2003@JohnB')
time.sleep(3)
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/login_button").click()
time.sleep(8)

# Navigate to the third item in the navigation bar
driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.singlepointsol.navigatioindrawerr:id/navigation_bar_item_icon_view"])[3]').click()
time.sleep(3)

# Step 4: Open Claim Section
# Click on the "Get Claim" button
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/claim_get_button").click()
time.sleep(5)

# Step 5: Enter Claim Details
# Clearing the existing text in the claim number field and entering a new claim number
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_no").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_no").send_keys('CLA1234564')
time.sleep(3)

# Step 6: Update Claim Details
# Enter claim date
claim_date = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/claim_date_et")
claim_date.click()
claim_date.send_keys('2025-01-30')
time.sleep(2)

# Enter policy number
policy_no = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_policy_no")
policy_no.send_keys('6789054321')
time.sleep(3)

# Enter incident date
incident_date = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_incident_date")
incident_date.click()
incident_date.send_keys('2025-01-02T12:53:00')
time.sleep(3)

# Enter incident location
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_incident_location").send_keys('Hyderabad')
time.sleep(3)

# Enter incident description
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_incident_description").send_keys('Rear-end collision at a traffic signal')
time.sleep(3)

# Enter claim amount
claim_amount = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_claim_amount"]')
claim_amount.send_keys('25000.0000')
time.sleep(3)

# Enter surveyor's name
SurveyerName = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/surveyname_et").send_keys('satwik')
time.sleep(2)

# Enter surveyor's phone number
SurveyerPhone = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_surveyPhone").send_keys('9638527419')
time.sleep(2)

# Enter survey date
Survey_date = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_survey_date")
Survey_date.click()
Survey_date.send_keys('2025-01-15')
time.sleep(3)

# Enter survey description
SurveyDescription = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_survey_desc").send_keys('Detailed inspection revealed minor damage')
time.sleep(3)

# Enter claim status
ClaimStatus = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_status").send_keys('S')
time.sleep(3)

# Step 7: Save Claim
# Click on the "Save" button to update the claim
Update_button = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/claim_save_button")
Update_button.click()
time.sleep(5)

# Re-enter claim details to verify updates
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_no").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_no").send_keys('CLA1234564')
time.sleep(3)

# Updating claim details again
claim_date = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/claim_date_et")
claim_date.click()
claim_date.send_keys('2025-01-30')
time.sleep(2)

policy_no = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_policy_no")
policy_no.send_keys('6789054321')
time.sleep(3)

incident_date = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_incident_date")
incident_date.click()
incident_date.send_keys('2025-01-02T12:53:00')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_incident_location").send_keys('Hyderabad')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_incident_description").send_keys('Rear-end collision at a traffic signal')
time.sleep(3)

claim_amount = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_claim_amount"]')
claim_amount.send_keys('27000.0000')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/surveyname_et").send_keys('satwikgoud')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_surveyPhone").send_keys('9638527456')
time.sleep(2)

Survey_date = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_survey_date")
Survey_date.click()
Survey_date.send_keys('2025-01-15')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_survey_desc").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_survey_desc").send_keys('Detailed inspection revealed minor damages')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_status").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_status").send_keys('T')
time.sleep(3)

# Click on the "Update" button to save changes
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/claim_update_button").click()
time.sleep(5)

# Delete the claim
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/et_claim_no").send_keys('CLA1234564')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/claim_delete_button").click()
time.sleep(5)
