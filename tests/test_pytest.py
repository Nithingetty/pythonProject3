from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.ID,"Password" ).send_keys("admin123")



