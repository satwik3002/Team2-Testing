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

# Step 4: Open Navigation Drawer
# Click on the navigation drawer button (hamburger icon)
driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Navigation Drawer"]').click()
time.sleep(2)

# Step 5: Select Product from the Dropdown Menu
# Locate and click on the dropdown menu
dropdown = driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/title_tagline")
dropdown.click()
time.sleep(2)

# Select "Product" from the dropdown options
driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Product"]').click()
time.sleep(2)

# Step 6: Get Product Details
# Click the "Get" button to retrieve product details
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/product_get_button").click()
time.sleep(5)

# Step 7: Save Product Details
# Clear the Product ID field and enter a new Product ID
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/Dropdown_ProductId").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/Dropdown_ProductId").send_keys('PROD201113')
time.sleep(2)

# Enter product name
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productName_editText").send_keys('Comprehensive Car Plan')
time.sleep(2)

# Enter product description
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productDesc_editText").send_keys('Full coverage for personal cars')
time.sleep(2)

# Enter product UIN (Unique Identification Number)
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productUIN_editText").send_keys('UINCAR12345698756456')
time.sleep(2)

# Enter insured interests
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/insuredIntrests_editText").send_keys('private car')
time.sleep(2)

# Enter policy coverage details
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/policyCoverage_editText").send_keys('Collision, Theft, Natural Calamities')
time.sleep(2)

# Click the "Save" button to save the product details
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/product_save_button").click()
time.sleep(2)

# Step 8: Update Product Details
# Clear the Product ID field and enter the existing Product ID
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/Dropdown_ProductId").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/Dropdown_ProductId").send_keys('PROD201113')

# Enter the updated product name
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productName_editText").send_keys('Comprehensive Car Plan')
time.sleep(2)

# Update product description
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productDesc_editText").send_keys('Full coverage for personal cars')
time.sleep(2)

# Clear and update the product UIN
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productUIN_editText").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/productUIN_editText").send_keys('UINCAR12345698756654')
time.sleep(2)

# Clear and update insured interests
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/insuredIntrests_editText").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/insuredIntrests_editText").send_keys('public car')
time.sleep(2)

# Update policy coverage details
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/policyCoverage_editText").send_keys('Collision, Theft, Natural Calamities')
time.sleep(2)

# Click the "Update" button to save changes
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/product_update_button").click()
time.sleep(2)

# Step 9: Delete Product
# Clear the Product ID field and enter the Product ID to be deleted
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/Dropdown_ProductId").clear()
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/Dropdown_ProductId").send_keys('PROD201113')
time.sleep(2)

# Click the "Delete" button to remove the product
driver.find_element(AppiumBy.ID, "com.singlepointsol.navigatioindrawerr:id/product_delete_button").click()
time.sleep(2)
