from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1: Desired Capabilities
# These settings define the device and app to be used in the automation
desired_caps = {
    "platformName": "Android",  # Target platform
    "appium:automationName": "UiAutomator2",  # Automation engine
    "appium:platformVersion": "15",  # Android version
    "appium:deviceName": "emulator-5554",  # Device name
    "app": "D:\\TestAPK\\app-debug.apk"  # Path to the APK file to test
}

# Step 2: Create Driver Object
# Establish a connection to the Appium server and load the app
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(15)  # Wait for the app to load

# Step 3: Navigate to the Registration Page
# Click on the "Register" button to open the registration form
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/register_textButton").click()
time.sleep(5)

# Step 4: Enter Registration Details
# Enter the user's name
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/name_et").send_keys('JohnA')
time.sleep(3)

# Enter the email address
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/registeremail_editText").send_keys('JohnA@gmail.com')
time.sleep(3)

# Enter the phone number
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/phone_et").send_keys('7534128965')
time.sleep(3)

# Enter the password
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/password_editText").send_keys('2003@JohnA')
time.sleep(3)

# Confirm the password
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/confirmpassword_editText").send_keys('2003@JohnA')
time.sleep(3)

# Step 5: Complete Registration
# Click the "Register" button to submit the form
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/register").click()
time.sleep(3)
