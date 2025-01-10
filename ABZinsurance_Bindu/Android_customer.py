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
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/vehicle_textView').click()
time.sleep(10)
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/email_editText"]').send_keys("bindhi@gmail.com") # Replace with actual button ID
time.sleep(10)
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/password_editText"]').send_keys("QWer@123")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/login_button"]').click()
time.sleep(5)
# Home
driver.find_element(AppiumBy.XPATH,' //android.widget.ImageButton[@content-desc="Open Navigation Drawer"]').click()
time.sleep(5)
# Customer
driver.find_element(AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/design_menu_item_text" and @text="Customer"]  ').click()
time.sleep(5)

# Customer ID
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_id').send_keys("CUS1277567")
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_name').send_keys("Likitha")
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_phone').send_keys("9898989898")
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_email').send_keys("aswsedd@gmail.com")
time.sleep(5)
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/customer_address"]').send_keys("Hyderabad")
time.sleep(5)
# Save button
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/btn_save"]').click()
time.sleep(5)
# Get button
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/btn_get"]').click()
time.sleep(10)
#update
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_id').send_keys("CUS1277567")
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_name').send_keys("Likitha Gunda")
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_phone').send_keys("9898989898")
time.sleep(5)
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_email').send_keys("aswsedd@gmail.com")
time.sleep(5)
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/customer_address"]').send_keys("Hyderabad")
time.sleep(5)
# Save button
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/btn_update').click()
time.sleep(5)

#delete
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/customer_id').send_keys("CUS1274567")
time.sleep(5)


driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/btn_delete').click()
time.sleep(5)

# Step 5 : Close the driver object
driver.quit()