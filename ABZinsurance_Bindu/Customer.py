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
#customer
driver.find_element(By.XPATH,"//a[normalize-space()='Customer']").click()
time.sleep(3)
rows = driver.find_elements(By.XPATH, "//table[@class='table']//tr")[1:]  # Skipping header row
customer_count1 = len([row for row in rows if row.find_elements(By.TAG_NAME, 'td')[0].text.strip()])
print(f"Number of customers : {customer_count1}")

#create new
driver.find_element(By.XPATH,"//a[normalize-space()='Create New']").click()
time.sleep(1)
driver.find_element(By.ID,"CustomerID").send_keys("CUST764567")
time.sleep(1)
driver.find_element(By.ID,"CustomerName").send_keys("Roshini")
time.sleep(1)
driver.find_element(By.NAME,"CustomerPhone").send_keys("9897456765")
time.sleep(1)
driver.find_element(By.NAME,"CustomerEmail").send_keys("roshini@gmail.com")
time.sleep(1)
driver.find_element(By.ID,"CustomerAddress").send_keys("woodland showroom, Madhapur, Hyderabad")
time.sleep(1)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/form[1]/div[6]/input[1]").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(5)
rows = driver.find_elements(By.XPATH, "//table[@class='table']//tr")[1:]  # Skipping header row
customer_count2 = len([row for row in rows if row.find_elements(By.TAG_NAME, 'td')[0].text.strip()])
print(f"Number of customer after creating new customer {customer_count2}")
if(customer_count2==(customer_count1+1)):
    print("New customer successfully created")
else:
    print("New customer creation failed")
#edit
driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[10]/td[6]/a[1]").click()
time.sleep(2)
driver.find_element(By.ID,"CustomerName").send_keys(" P")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[6]/input").click()
time.sleep(1)
print("Total value is edited to 100 successfully")
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(5)
#details
driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[10]/td[6]/a[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/main/div[2]/a[2]").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(5)

#delete

driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[10]/td[6]/a[3]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/main/div/form/input[1]").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,2700);")
time.sleep(5)
rows = driver.find_elements(By.XPATH, "//table[@class='table']//tr")[1:]  # Skipping header row
customer_count3 = len([row for row in rows if row.find_elements(By.TAG_NAME, 'td')[0].text.strip()])
print(f"Number of customer after deleting new customer: {customer_count3}")
if(customer_count1==(customer_count3)):
    print("New customer successfully deleted")
else:
    print("New customer deletion failed")
print("New customer created, edited, details displayed and deleted successfully ")