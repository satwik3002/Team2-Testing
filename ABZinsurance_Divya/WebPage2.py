import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime



driver = webdriver.Chrome()
driver.get("http://abzvehiclemvcwebapp-akshitha.azurewebsites.net/")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul[2]/li[1]/a").click()  # Register
time.sleep(4)

driver.find_element(By.ID, "Input_Email").send_keys("divyachemitikanti7@gmail.com")  # E-mail
time.sleep(2)

driver.find_element(By.NAME, "Input.Password").send_keys("Divya@2001")  # Password
time.sleep(4)

driver.find_element(By.ID, "Input_ConfirmPassword").send_keys("Divya@2001")  # confirm-password
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="registerSubmit"]').click()  # Registration button
time.sleep(5)
assert "Register - ABZVehicleInsuranceMvcProject" in driver.page_source or "Confirm your account" in driver.page_source, "Registration failed or no confirmation required."  # Registration title



driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul[2]/li[2]/a").click()  # Login
time.sleep(4)

driver.find_element(By.ID, "Input_Email").send_keys("divyachemitikanti7@gmail.com")  # E-mail
time.sleep(2)

driver.find_element(By.NAME, "Input.Password").send_keys("Divya@2001")  # Password
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()  # login button
time.sleep(4)

assert "Home Page - ABZVehicleInsuranceMvcProject" in driver.page_source, "Login failed."  # Login Title
driver.find_element(By.XPATH, "//a[normalize-space()='Agent']").click()  # navigate to Agent
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/main/p/a").click()  # navigate to create new
time.sleep(2)

edit_box = driver.find_element(By.XPATH, '//*[@id="AgentID"]')  # AgentID
edit_box.send_keys("1234567890")
time.sleep(2)

edit_box = driver.find_element(By.NAME, "AgentName")  # Agent Name
edit_box.send_keys("Divya")
time.sleep(2)

edit_box = driver.find_element(By.ID, "AgentPhone")  # Agent Phone
edit_box.send_keys("6801257274")
time.sleep(2)

edit_box = driver.find_element(By.ID, "AgentEmail")  # Agent Email
edit_box.send_keys("diya@gmail.com")
time.sleep(2)

edit_box = driver.find_element(By.ID, "LicenseCode")  # License code
edit_box.send_keys("2345676789")
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/form/div[6]/input").click()  # create btn
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul[1]/li[6]/a").click()  # policy
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/main/p/a").click()  # navigate to create new
time.sleep(2)

driver.find_element(By.ID, "PolicyNo").send_keys("7890123456")  # policy number
time.sleep(2)

driver.find_element(By.NAME,"ProposalNo").click()       #proposal no
time.sleep(2)

edit_box = driver.find_element(By.ID, "NoClaimBonus")  # No Claim Bonus
edit_box.send_keys("2345678901")
time.sleep(2)

edit_box = driver.find_element(By.ID, "ReceiptNo")  # Receipt number
edit_box.send_keys("54321")
time.sleep(2)

driver.find_element(By.ID, "ReceiptDate").send_keys("01-01-2024")  # Receipt Date
time.sleep(2)

edit_box = driver.find_element(By.ID, "PaymentMode")  # PaymentMode
edit_box.send_keys("U")
time.sleep(2)

edit_box = driver.find_element(By.ID, "Amount")  # Amount
edit_box.send_keys("10000")
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/form/div[8]/input").click()  # create btn
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[1]/li[7]/a").click()        #Click Agent
time.sleep(2)

dropdown_element = driver.find_element(By.ID,"dropdownMenuButton").click()       #action dropdown
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/div/ul/li[1]/a").click()          #edit
time.sleep(2)

driver.find_element(By.ID,"AgentName").send_keys(".Ch")            #edit agent name
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[6]/input").click()       #save btn
time.sleep(2)

dropdown_element = driver.find_element(By.ID,"dropdownMenuButton").click()       #action dropdown
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/div/ul/li[2]/a").click()     #details
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/div[2]/a[2]").click()         #back to list
time.sleep(2)

dropdown_element = driver.find_element(By.ID,"dropdownMenuButton").click()       #action dropdown
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/div/ul/li[3]/a").click()          #delete btn
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/div/form/input[1]").click()         #click delete
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[1]/li[6]/a").click()       #navigate to policy
time.sleep(2)

dropdown_element = driver.find_element(By.ID,"dropdownMenuButton").click()       #action dropdown     #policy
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[8]/div/ul/li[1]/a").click()         #edit
time.sleep(2)

#driver.find_element(By.NAME,'ReceiptNo').send_keys("h")      #payment
#time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[8]/input").click()      #save
time.sleep(2)

dropdown_element = driver.find_element(By.ID,"dropdownMenuButton").click()         #action dropdown
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[8]/div/ul/li[4]/a").click()      #add-on
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/p/a").click()    #Create new
time.sleep(2)

driver.find_element(By.ID,"AddonID").send_keys("4325")    #addon id
time.sleep(2)

driver.find_element(By.NAME,"PolicyNo").click()   #policy no
time.sleep(2)

driver.find_element(By.NAME,"Amount").send_keys("10000")     #amount
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[4]/input").click()      #create btn
time.sleep(2)










