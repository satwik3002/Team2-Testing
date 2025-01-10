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
time.sleep(10)

nav_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Navigation Drawer"]')))
nav_button.click()

Agent_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.singlepointsol.navigatioindrawerr:id/nav_agent")')
Agent_btn.click()
time.sleep(3)

#driver.find_element(AppiumBy.ID,"com.singlepointsol.navigatioindrawerr:id/text_input_end_icon").click()        # agent id dropdown
#time.sleep(2)



driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/dropdown_agent_id"]').send_keys('5764327867')          #agent id
time.sleep(3)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_name"]').send_keys('Divya')       #agent name
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_phone"]').send_keys('6801247687')          #agent phone number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_Agent_email"]').send_keys('divyach74@gmail.com')       #agent email
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_license_code"]').send_keys('9876')        #licence code
time.sleep(2)

Savebtn = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/agent_save_button"]')        #save btn
Savebtn.click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/dropdown_agent_id"]').send_keys('98rgh')          #agent id
time.sleep(3)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_name"]').send_keys('Divya')       #agent name
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_phone"]').send_keys('6801247687')          #agent phone number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_Agent_email"]').send_keys('divyach74@gmail.com')       #agent email
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_license_code"]').send_keys('9876')        #licence code
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/agent_get_button"]').click()         #get btn
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/dropdown_agent_id"]').send_keys('5764327867')          #agent id
time.sleep(3)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_name"]').send_keys('Divya')       #agent name
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_phone"]').send_keys('6801247687')          #agent phone number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_Agent_email"]').send_keys('divyach74@gmail.com')       #agent email
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_license_code"]').send_keys('9876')        #licence code
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/agent_updadte_button"]').click()        #update btn
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/dropdown_agent_id"]').send_keys('5764327867')          #agent id
time.sleep(3)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_name"]').send_keys('Divya')       #agent name
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_agent_phone"]').send_keys('6801247687')          #agent phone number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_Agent_email"]').send_keys('divyach74@gmail.com')       #agent email
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_license_code"]').send_keys('9876')        #licence code
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/agent_delete_button"]').click()        #delete button
time.sleep(2)










