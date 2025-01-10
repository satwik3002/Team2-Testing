import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

desired_caps={
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "emulator-5554",
  "appium:ensureWebviewsHavePages": "true",
  "appium:nativeWebScreenshot": "true",
  "appium:newCommandTimeout": 8000,
  "appium:connectHardwareKeyboard": "true",
  "appium:appPackage": "com.singlepointsol.navigatioindrawerr",
  "appium:appActivity": "com.singlepointsol.navigatioindrawerr.SplashScreenActivity"
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723",options=options)
time.sleep(2)

#ele_id = driver.find_element_by_id_("com.singlepointsol.navigatioindrawerr:id/EnterValue")
#ele_id.click()

email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/email_editText")))
email_field.send_keys('divyachemitikanti7@gmail.com')


#driver.find_element(AppiumBy.ID,"com.singlepointsol.navigatioindrawerr:id/email_editText").send_keys('divyachemitikanti7@gmail.com')
#time.sleep(3)

driver.find_element(AppiumBy.ID,"com.singlepointsol.navigatioindrawerr:id/password_editText").send_keys('Divya@2001')
time.sleep(3)

Login = driver.find_element(AppiumBy.ID,"com.singlepointsol.navigatioindrawerr:id/login_button")
Login.click()
time.sleep(3)

nav_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Navigation Drawer"]')))
nav_button.click()

driver.find_element(AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.singlepointsol.navigatioindrawerr:id/nav_policy"]').click()
time.sleep(2)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Policy Addons")').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[1]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/addon_id_et"]').send_keys("9876")        #add on id
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/policy_no_et"]').send_keys("8317597442")       #policy number
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/amount_et"]').send_keys("2000")        #amount
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/policyaddon_save_button"]').click()         #save btn
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[1]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/addon_id_et"]').send_keys("8317")        #add on id
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/policy_no_et"]').send_keys("6789054321")       #policy number
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/amount_et"]').send_keys("500.0000")        #amount
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/policyaddon_get_button"]').click()         #get btn
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[1]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/addon_id_et"]').send_keys("9542")        #add on id
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/policy_no_et"]').send_keys("6789054321")       #policy number
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/amount_et"]').send_keys("500.0000")        #amount
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/policyaddondelete_button"]').click()          #delete btn
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button1"]').click()       #delete alert
time.sleep(2)












