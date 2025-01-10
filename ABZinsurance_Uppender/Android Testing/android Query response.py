from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1 : Create "Desired Capabilities"
desired_caps ={
    "platformName" : "Android",
    "appium:automationName" : "UiAutomator2",
    "appium:platformVersion" : "15",
    "appium:deviceName" : "emulator-5554",
    "appium:appPackage" : "com.singlepointsol.navigatioindrawerr",
    "appium:appActivity" : ".SplashScreenActivity"
}

# Step 2 : Create "Driver object"
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723",options=options)

time.sleep(10)

driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/email_editText"]').send_keys("bindhi@gmail.com")
time.sleep(10)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/password_editText"]').send_keys("QWer@123")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/login_button"]').click()
time.sleep(5)

# Home
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageButton[@content-desc="Open Navigation Drawer"]').click()
time.sleep(5)

# Query Response
driver.find_element(AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/design_menu_item_text" and @text="Query Response"]').click()
time.sleep(5)

# Create New Query Response
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_create_button"]').click()
time.sleep(5)

# Enter Query Response Details
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/query_response_id').send_keys("QRY12345")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_customer_id"]').send_keys("CUST12345")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_description"]').send_keys("Test Query Response")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_date"]').send_keys("2024-11-12")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_status"]').send_keys("A")
time.sleep(5)

# Save Query Response
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_save_button"]').click()
time.sleep(5)

# Update Query Response
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/query_response_id').send_keys("QRY12345")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_customer_id"]').send_keys("CUST12345")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_description"]').send_keys("Test Query Response Updated")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_date"]').send_keys("2024-11-12")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_status"]').send_keys("A")
time.sleep(5)

# Update Query Response
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/query_response_update_button"]').click()
time.sleep(5)
driver.quit()