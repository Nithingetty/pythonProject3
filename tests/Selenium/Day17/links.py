from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")

#links = driver.find_elements(By.TAG_NAME, 'a')
links = driver.find_elements(By.XPATH, '//a')


print("total number of links ", len(links))

for link in links:
    print(link.text)
