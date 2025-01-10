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

#Policy_Button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.singlepointsol.navigatioindrawerr:id/nav_policy")')
#Policy_Button.click()
#time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Policy"]').click()
time.sleep(2)

#Policy_Button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.singlepointsol.navigatioindrawerr:id/nav_policy")')
#Policy_Button.click()
#time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_policy_no"]').send_keys("6789054321")    #policy number
time.sleep(2)

#driver.find_element(AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.singlepointsol.navigatioindrawerr:id/inputLayoutPolicyNo"]/android.widget.FrameLayout/android.widget.LinearLayout').click()
#time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[1]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_proposal_no"]').send_keys("7890654321")     #proposal number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_no_claim_bonus"]').send_keys("15.0000")     #no claim bonus
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_receipt_no"]').send_keys("abcdg")     #receipt number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_receipt_date"]').send_keys("2025-01-05T00:00:00")     #receipt date
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[3]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/payment_mode_et"]').send_keys("D")      #payment mode
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_amount"]').send_keys("9700.0000")      #amount
time.sleep(2)

driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/btn_get').click()                 #get btn
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_policy_no"]').send_keys("9532987078")    #policy number
time.sleep(2)

#driver.find_element(AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.singlepointsol.navigatioindrawerr:id/inputLayoutPolicyNo"]/android.widget.FrameLayout/android.widget.LinearLayout').click()
#time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[1]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_proposal_no"]').send_keys("7890654321")     #proposal number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_no_claim_bonus"]').send_keys("15.0000")     #no claim bonus
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_receipt_no"]').send_keys("12345")     #receipt number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_receipt_date"]').send_keys("2025-01-05T00:00:00")     #receipt date
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[3]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/payment_mode_et"]').send_keys("U")      #payment mode
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_amount"]').send_keys("9800.0000")      #amount
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/btn_post"]').click()                #save btn
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_policy_no"]').send_keys("6789054321")    #policy number
time.sleep(2)

#driver.find_element(AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.singlepointsol.navigatioindrawerr:id/inputLayoutPolicyNo"]/android.widget.FrameLayout/android.widget.LinearLayout').click()
#time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[1]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_proposal_no"]').send_keys("7890654321")     #proposal number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[2]').click()
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_no_claim_bonus"]').send_keys("225.0000")     #no claim bonus
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_receipt_no"]').send_keys("abcdg")     #receipt number
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_receipt_date"]').send_keys("2025-01-05T00:00:00")     #receipt date
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageButton[@content-desc="Show dropdown menu"])[3]').click()
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/payment_mode_et"]').send_keys("C")      #payment mode
time.sleep(2)

driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_amount"]').send_keys("87000.0000")      #amount
time.sleep(2)


driver.find_element(AppiumBy.ID,'com.singlepointsol.navigatioindrawerr:id/btn_put').click()                #update btn
time.sleep(2)


driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.singlepointsol.navigatioindrawerr:id/et_policy_no"]').send_keys("9505404078")    #policy number
time.sleep(2)



driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.singlepointsol.navigatioindrawerr:id/btn_delete"]').click()        #delete btn
time.sleep(2)



