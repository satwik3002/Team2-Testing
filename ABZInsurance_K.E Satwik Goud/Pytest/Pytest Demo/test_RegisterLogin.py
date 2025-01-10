import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_register_user(driver):
    driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/')
    time.sleep(10)

    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    time.sleep(5)

    driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
    time.sleep(5)
    driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
    time.sleep(5)
    driver.find_element(By.ID, "Input_ConfirmPassword").send_keys('2003@JohnB')
    time.sleep(5)

    driver.find_element(By.ID, "registerSubmit").click()
    time.sleep(5)


def test_login_user(driver):
    driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/')
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    time.sleep(5)

    driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
    time.sleep(5)
    driver.find_element(By.ID, "Input_Password").send_keys('2003@JohnB')
    time.sleep(5)
    driver.find_element(By.ID, "Input_RememberMe").click()
    time.sleep(5)

    driver.find_element(By.ID, "login-submit").click()
    time.sleep(5)


def test_reset_password(driver):
    driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[@id='forgot-password']").click()
    time.sleep(5)

    driver.find_element(By.ID, "Input_Email").send_keys('JohnB@gmail.com')
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Reset Password']").click()
    time.sleep(5)


def test_register_new_user(driver):
    driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
    time.sleep(10)
    driver.find_element(By.XPATH, "//a[normalize-space()='Register as a new user']").click()
    time.sleep(5)

    driver.find_element(By.ID, "Input_Email").send_keys('BBb@gmail.com')
    time.sleep(5)
    driver.find_element(By.ID, "Input_Password").send_keys('2003@BBb')
    time.sleep(5)
    driver.find_element(By.ID, "Input_ConfirmPassword").send_keys('2003@BBb')
    time.sleep(5)

    driver.find_element(By.ID, "registerSubmit").click()
    time.sleep(5)


def test_resend_email(driver):
    driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Identity/Account/Login')
    time.sleep(5)

    driver.find_element(By.ID, "resend-confirmation").click()
    time.sleep(5)

    driver.find_element(By.ID, "Input_Email").send_keys('BBb@gmail.com')
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Resend']").click()
    time.sleep(5)


def test_create_claim(driver):
    # Navigate to Claims section
    driver.get('https://abzvehiclemvcwebapp-akshitha.azurewebsites.net/Claim')
    time.sleep(3)

    # Create a new claim
    driver.find_element(By.XPATH, "//a[contains(text(),'Create New')]").click()
    driver.find_element(By.ID, "ClaimNo").send_keys('CLC1234564')
    time.sleep(3)

    # Select Claim Date
    claim_date = driver.find_element(By.ID, "ClaimDate")
    ActionChains(driver).move_to_element_with_offset(claim_date, 10, 0).click().perform()
    claim_date.send_keys('12-31-2024')
    time.sleep(2)

    # Select Incident Date
    incident_date = driver.find_element(By.ID, "IncidentDate")
    ActionChains(driver).move_to_element_with_offset(incident_date, 10, 0).click().perform()
    incident_date.send_keys('12-12-2024')
    time.sleep(2)

    # Fill out other claim details
    driver.find_element(By.ID, "IncidentLocation").send_keys('HYD')
    driver.find_element(By.ID, "IncidentDescription").send_keys('Rear-end collision at a traffic signal involving a private car and a truck')
    driver.find_element(By.ID, "ClaimAmount").clear()
    driver.find_element(By.ID, "ClaimAmount").send_keys('25000')
    driver.find_element(By.ID, "SurveyorName").send_keys('Rahul Verma')
    driver.find_element(By.ID, "SurveyorPhone").send_keys('9876543210')
    time.sleep(2)

    # Select Survey Date
    survey_date = driver.find_element(By.ID, "SurveyDate")
    ActionChains(driver).move_to_element_with_offset(survey_date, 10, 0).click().perform()
    survey_date.send_keys('12-30-2024')
    time.sleep(2)

    # Add Survey Description and Claim Status
    driver.find_element(By.ID, "SurveyDescription").send_keys('Detailed inspection revealed minor damage to the rear bumper and taillight')
    driver.find_element(By.ID, "ClaimStatus").send_keys('S')
    time.sleep(2)

    # Submit the claim
    driver.find_element(By.XPATH, "//input[@value='Create']").click()
    time.sleep(5)

