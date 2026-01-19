
#we need to install request package through file-->Settings ---->projectinterpreter
from playwright.sync_api import expect
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests
from selenium.webdriver.support.expected_conditions import none_of

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")

alllinks = driver.find_elements(By.TAG_NAME, 'a')
count=0

for link in alllinks:
    url = link.get_attribute("href")

    if url is None or url.startswith("javascript") or url.startswith("mailto"):
        continue

    try:
        res = requests.head(url, timeout=5)
        if res.status_code >= 400:
            print(url, "is broken link")
            count += 1
        else:
            print(url, "is valid link")

    except requests.exceptions.RequestException as e:
        print(url, "is broken due to exception")
        count += 1

print("Total number of broken links:", count)