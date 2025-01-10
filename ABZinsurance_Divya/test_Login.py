import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://abzvehiclemvcwebapp-akshitha.azurewebsites.net/")

    driver.maximize_window()
    yield driver
    driver.quit()


def test_registration(driver):
    driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[2]/li[1]/a").click()       #Register
    time.sleep(4)

    driver.find_element(By.ID, "Input_Email").send_keys("divyachemitikanti7@gmail.com")      #E-mail
    time.sleep(2)

    driver.find_element(By.NAME,"Input.Password").send_keys("Divya@2001")           #Password
    time.sleep(4)

    driver.find_element(By.ID, "Input_ConfirmPassword").send_keys("Divya@2001")        #confirm-password
    time.sleep(4)

    driver.find_element(By.XPATH,'//*[@id="registerSubmit"]').click()     #Registration button
    time.sleep(5)
    assert "Register - ABZVehicleInsuranceMvcProject" in driver.page_source or "Confirm your account" in driver.page_source, "Registration failed or no confirmation required."     #Registration title


def test_login(driver):
    driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[2]/li[2]/a").click()       #Login
    time.sleep(4)

    driver.find_element(By.ID, "Input_Email").send_keys("divyachemitikanti7@gmail.com")   #E-mail
    time.sleep(2)

    driver.find_element(By.NAME, "Input.Password").send_keys("Divya@2001")          #Password
    time.sleep(4)

    driver.find_element(By.XPATH,'//*[@id="login-submit"]').click()    #login button
    time.sleep(4)

    assert "Home Page - ABZVehicleInsuranceMvcProject" in driver.page_source, "Login failed."                #Login Title

def test_agent(driver):
    driver.find_element(By.XPATH,"//a[normalize-space()='Agent']").click()#navigate to Agent
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/p/a").click()     #navigate to create new
    time.sleep(2)

    edit_box = driver.find_element(By.XPATH,'//*[@id="AgentID"]')          #AgentID
    edit_box.send_keys("1234567890")
    time.sleep(2)

    edit_box = driver.find_element(By.NAME,"AgentName")            #Agent Name
    edit_box.send_keys("Divya")
    time.sleep(2)

    edit_box = driver.find_element(By.ID,"AgentPhone")                #Agent Phone
    edit_box.send_keys("6801257274")
    time.sleep(2)


    edit_box = driver.find_element(By.ID,"AgentEmail")              #Agent Email
    edit_box.send_keys("diya@gmail.com")
    time.sleep(2)

    edit_box = driver.find_element(By.ID,"LicenseCode")                #License code
    edit_box.send_keys("2345676789")
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[6]/input").click()            #create btn
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/a[1]").click()        #edit
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[6]/input").click()         #save
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/a[2]").click()         #details
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/div[2]/a[2]").click()        #back to list
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/a[3]").click()       #delete
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/div/form/a").click()    #back to list
    time.sleep(2)



def test_policy(driver):
    driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[1]/li[6]/a").click()    #policy
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div/main/p/a").click()  # navigate to create new
    time.sleep(2)

    driver.find_element(By.ID, "PolicyNo").send_keys("7890123456")          #policy number
    time.sleep(2)

    edit_box = driver.find_element(By.ID,"NoClaimBonus")    #No Claim Bonus
    edit_box.send_keys("2345678901")
    time.sleep(2)

    edit_box = driver.find_element(By.ID,"ReceiptNo")            #Receipt number
    edit_box.send_keys("54321")
    time.sleep(2)

    driver.find_element(By.ID, "ReceiptDate").send_keys("01-01-2024")        #Receipt Date
    time.sleep(2)

    edit_box = driver.find_element(By.ID,"PaymentMode")         #PaymentMode
    edit_box.send_keys("U")
    time.sleep(2)

    edit_box = driver.find_element(By.ID, "Amount")        #Amount
    edit_box.send_keys("10000")
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[8]/input").click()        #create btn
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[8]/a[1]").click()     #edit
    time.sleep(2)

    

    driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[8]/input").click()       #save
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[2]/td[8]/a[2]").click()       #details
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/div[2]/a[2]").click()              #back to list
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[2]/td[8]/a[3]").click()        #delete
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/div/form/input[1]").click()           #delete btn
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[8]/a[4]").click()        #addon
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/p/a").click()        #create new
    time.sleep(2)

    edit_box = driver.find_element(By.NAME,"AddonID")      #addon Id
    edit_box.send_keys("1234")
    time.sleep(2)

    driver.find_element(By.ID,"PolicyNo").click()         #click policy no
    time.sleep(2)

    edit_box = driver.find_element(By.NAME,"Amount")         #amount
    edit_box.send_keys("10000")
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[4]/input").click()             #create btn
    time.sleep(2)


    driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr/td[4]/a[3]").click()          #delete btn
    time.sleep(2)




