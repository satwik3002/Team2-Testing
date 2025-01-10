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
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/email_editText"]').send_keys("bindhi@gmail.com") # Replace with actual button ID
time.sleep(10)
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/password_editText"]').send_keys("QWer@123")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/login_button"]').click()
time.sleep(5)
# Home
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageButton[@content-desc="Open Navigation Drawer"]').click()
time.sleep(5)
# Proposal
driver.find_element(AppiumBy.XPATH,'//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="com.singlepointsol.navigatioindrawerr:id/nav_proposal"]').click()
time.sleep(5)


# Get button
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/proposal_get_button').click()
time.sleep(10)
# Delete
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/proposal_no_EditText').send_keys("Pro0067890")
time.sleep(5)
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/proposal_delete_button"]').click()
time.sleep(10)
