from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/")
driver.maximize_window()
time.sleep(1)

# Login
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
time.sleep(1)
# Details of login
driver.find_element(By.ID,"Input_Email").send_keys("bindhi@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"Input.Password").send_keys("QWer@123")
time.sleep(1)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/section[1]/form[1]/div[4]/button[1]").click()
time.sleep(1)
#proposal
driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/nav[1]/div[1]/div[1]/ul[1]/li[5]/a[1]").click()
time.sleep(1)
#proposal count
rows = driver.find_elements(By.XPATH, "//table[@class='table']//tr")[1:]  # Skipping header row
proposal_count = len([row for row in rows if row.find_elements(By.TAG_NAME, 'td')[0].text.strip()])
print(f"Number of proposals: {proposal_count}")
#create new
driver.find_element(By.XPATH,"//a[normalize-space()='Create New']").click()
time.sleep(1)
##proposal id
driver.find_element(By.ID,"ProposalNo").send_keys("PROP954555")
time.sleep(1)
##vehicle id
driver.find_element(By.XPATH, "//select[@id='RegNo']//option[text()='VEHI954954']").click()
time.sleep(1)
##product id
driver.find_element(By.XPATH,"//select[@id='ProductID']//option[text()='PROD954954']").click()
time.sleep(1)
##customer id
driver.find_element(By.XPATH,"//select[@id='CustomerID']//option[text()='CUST954954']").click()
time.sleep(1)
##agent id
driver.find_element(By.XPATH,"//select[@id='AgentID']//option[text()='AGEN954954']").click()
time.sleep(1)
## from date and to date
driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[5]/input[1]").send_keys("01-01-2024")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='ToDate']").send_keys("01-01-2025")
time.sleep(1)
## IDV value
driver.find_element(By.ID,"IDV").clear()
driver.find_element(By.ID,"IDV").send_keys("10")
time.sleep(1)
## Basic amount
driver.find_element(By.NAME,"BasicAmount").send_keys("80")
time.sleep(1)
## Total amount
driver.find_element(By.NAME,"TotalAmount").send_keys("90")
time.sleep(1)
##save button
driver.find_element(By.XPATH,"//input[@value='Create']").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(1)
#checking if new proposal is added
#proposal count
rows = driver.find_elements(By.XPATH, "//table[@class='table']//tr")[1:]  # Skipping header row
proposal_count1 = len([row for row in rows if row.find_elements(By.TAG_NAME, 'td')[0].text.strip()])
print(f"Number of proposals after creating new proposal: {proposal_count1}")
if(proposal_count1==(proposal_count+1)):
    print("New proposal successfully created")
else:
    print("New proposal creation failed")

#edit
driver.find_element(By.XPATH,"//tbody/tr[6]/td[11]/a[1]").click()
time.sleep(1)
driver.find_element(By.ID,"TotalAmount").clear()
driver.find_element(By.ID,"TotalAmount").send_keys("100")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='Save']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(1)
print("New proposal edited successfully")

#details
driver.find_element(By.XPATH,"//tbody/tr[6]/td[11]/a[2]").click()
time.sleep(15)
url1="https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Proposal/Details?proposalNo=PROP954555"
url2=driver.current_url
if(url1==url2):
    print("New proposal  details opened successfully")
else:
    print("New proposal details failed")
driver.find_element(By.XPATH,"//a[normalize-space()='Back to List']").click()
time.sleep(1)

#delete
driver.find_element(By.XPATH,"//tbody/tr[6]/td[11]/a[3]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='Delete']").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(1)
#
rows = driver.find_elements(By.XPATH, "//table[@class='table']//tr")[1:]  # Skipping header row
proposal_count2 = len([row for row in rows if row.find_elements(By.TAG_NAME, 'td')[0].text.strip()])
print(f"Number of proposals after deleting new proposal: {proposal_count2}")
if(proposal_count==proposal_count2):
    print("New proposal successfully deleted")
else:
    print("New proposal deletion failed")
print("New proposal is created, edited, details displayed and deleted succesfully")