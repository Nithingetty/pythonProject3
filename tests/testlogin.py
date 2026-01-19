from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    wait = WebDriverWait(driver, 15)

    username = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username.send_keys("Admin")

    password = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.send_keys("admin123")

    driver.quit()


#test_google_title()