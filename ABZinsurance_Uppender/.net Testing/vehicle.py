from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

# Open chrome and start the link
driver = webdriver.Chrome()
URL = "https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/"
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL)

# Checking the title
actual_title = driver.title
expected_title = "Home Page - ABZVehicleInsuranceMvcProject"
driver.save_screenshot(".//actual_title.png")
print(driver.title)
if actual_title == expected_title:
    print("Home page open Successfully")
else:
    print("Unsuccessful")

# Click on login button
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(1)

#Click on login button
# Click on Login
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(1)

# Fill login form
driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
driver.find_element(By.ID, "login-submit").click()
time.sleep(10)

#Navigate to vehicle page

Vehicle=driver.find_element(By.XPATH,"//a[normalize-space()='Vehicle']")
Vehicle.click()
#Click on create to create new vehicle registration
Create=driver.find_element(By.XPATH,"//a[normalize-space()='Create New']")
Create.click()

#Enter Details to Create a new vehicle Information
Reg_No=driver.find_element(By.ID,"RegNo")
Reg_No.send_keys("TS18G79191")

Reg_Authority=driver.find_element(By.ID,"RegAuthority")
Reg_Authority.send_keys("RTO,Nirmal ")

Make=driver.find_element(By.ID,"Make")
Make.send_keys("Tata")

Model=driver.find_element(By.ID,"Model")
Model.send_keys("Nano")

FuelType=driver.find_element(By.ID,"FuelType")
FuelType.send_keys("P")

Variant=driver.find_element(By.ID,"Variant")
Variant.send_keys("1000")

EngineNo=driver.find_element(By.ID,"EngineNo")
EngineNo.send_keys("Eng1234568789")

ChassisNO=driver.find_element(By.ID,"ChassisNo")
ChassisNO.send_keys("Chas123456789")

EngineCapacity=driver.find_element(By.ID,"EngineCapacity")
EngineCapacity.send_keys("1000")

SeatingCapacity=driver.find_element(By.ID,"SeatingCapacity")
SeatingCapacity.send_keys("4")

MfgYear=driver.find_element(By.ID,"MfgYear")
MfgYear.send_keys("2023")

RegDate=driver.find_element(By.ID,"RegDate")
RegDate.send_keys("1-Jan-2024")

BodyType=driver.find_element(By.ID,"BodyType")
BodyType.send_keys("Sedon")

LeasedBy=driver.find_element(By.ID,"LeasedBy")
LeasedBy.send_keys("Upendhar")
time.sleep(5)

driver.find_element(By.XPATH,"//select[@id='OwnerId']").send_keys("C123456789")
time.sleep(2)
actions = ActionChains(driver)
create_button = driver.find_element(By.XPATH, "//input[@value='Create']")
actions.move_to_element(create_button).click().perform()
time.sleep(3)

driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Vehicle')
time.sleep(5)

# Scroll to the required position to find the claim number
scroll_position = 1579
driver.execute_script(f"window.scrollTo(0, {scroll_position});")
time.sleep(4)
driver.quit()
