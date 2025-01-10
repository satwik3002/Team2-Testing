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

#Vehicle Registration
driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/design_menu_item_text" and @text="Vehicle"]').click()
time.sleep(5)

#Enter Vehicle Details
driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_reg_no').send_keys("TS18G79191")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_reg_authority').send_keys("RTO,Nirmal ")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_make').send_keys("Tata")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_model').send_keys("Nano")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_fuel_type').send_keys("P")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_variant').send_keys("1000")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_engine_no').send_keys("Eng1234568789")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_chassis_no').send_keys("Chas123456789")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_engine_capacity').send_keys("1000")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_seating_capacity').send_keys("4")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_mfg_year').send_keys("2023")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_reg_date').send_keys("1-Jan-2024")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_body_type').send_keys("Sedon")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_leased_by').send_keys("Upendhar")
time.sleep(5)

driver.find_element(AppiumBy.ID, 'com.singlepointsol.navigatioindrawerr:id/vehicle_owner_id').send_keys("C123456789")
time.sleep(5)
#save
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/customerquery_btn_save"]').click()
time.sleep(5)
#Update Vehicle
driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/vehicle_reg_no').send_keys("AP1234567")
time.sleep(5)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/vehicle_make"]').send_keys("Toyota")
time.sleep(5)
driver.quit()
