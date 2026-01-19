from re import search

from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\\Users\\NITHIN G\\Downloads\\chromedriver-win64_1\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://www.google.com/")

driver.maximize_window()
driver.implicitly_wait(10)

searchbox1=driver.find_element(By.ID, "APjFqb")

searchbox1.send_keys("selenium")

searchbox1.submit()
driver.find_element(By.CSS_SELECTOR, "h3.LC20lb").click()


