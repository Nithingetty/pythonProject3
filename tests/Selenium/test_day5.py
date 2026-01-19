from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\\Users\\NITHIN G\\Downloads\\chromedriver-win64_1\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

print(driver.current_url)
print(driver.title)



driver.quit()