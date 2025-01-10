from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1: Desired Capabilities
# These capabilities define the device and app under test
desired_caps = {
    "platformName": "Android",  # The platform to automate (Android)
    "appium:automationName": "UiAutomator2",  # Automation engine for Android
    "appium:platformVersion": "15",  # Android version of the device/emulator
    "appium:deviceName": "emulator-5554",  # Device/emulator identifier
    "app": "D:\\TestAPK\\app-debug.apk"  # Path to the app to be tested
}

# Step 2: Create Driver Object
# Establish a connection with the Appium server and load the specified options
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
time.sleep(15)  # Wait for the app to load

# Step 3: Login
# Entering email and password into the login fields and clicking the login button
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/email_editText").send_keys('JohnB@gmail.com')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/password_editText").send_keys('2003@JohnB')
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/login_button").click()
time.sleep(5)

driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Navigation Drawer"]').click()
time.sleep(5)

driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.singlepointsol.navigatioindrawerr:id/nav_product"]').click()
time.sleep(5)


driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Product Addons"]').click()
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddon_get_button").click()
time.sleep(5)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productId_dropdown").send_keys('PROD201112')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/addonId_dropdown").send_keys('A001234567')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddonTitle_editText").send_keys('Premium Support')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddonDesc_editText").send_keys('Provides 24/7 priority customer support.')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddon_Post_Button").click()
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productId_dropdown").send_keys('PROD201112')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/addonId_dropdown").send_keys('A001234567')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddonTitle_editText").send_keys('Premium Support')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddonDesc_editText").send_keys('Covers emergency roadside services')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddon_update_button").click()
time.sleep(3)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productId_dropdown").send_keys('PROD201112')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/addonId_dropdown").send_keys('A001234567')
time.sleep(2)

driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productAddon_delete_button").click()
time.sleep(3)





