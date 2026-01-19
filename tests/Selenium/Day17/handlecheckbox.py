from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()

driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
checkboxes = driver.find_elements(By.XPATH , "//input[@type='checkbox' and contains(@id,'id_check')]")

print(len(checkboxes))


#   approach1 selecting multiple checkboxes
for checkbox in checkboxes:
    checkbox.click()
#   approach2 selecting multiple checkboxes
for i in checkboxes :
    checkboxes[1].click()
    
    
driver.quit()