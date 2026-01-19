from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome driver setup
serv_obj = Service("C:\\Users\\NITHIN G\\Downloads\\chromedriver-win64_1\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open URL
driver.get("https://www.google.com/")
driver.maximize_window()

# Explicit wait object
wait = WebDriverWait(
    driver,
    10,
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException
    ]
)
# Wait for search box to be visible
searchbox1 = wait.until(
    EC.visibility_of_element_located((By.ID, "APjFqb"))
)

searchbox1.send_keys("selenium")
searchbox1.submit()

# Wait for search result and click first link
first_result = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.LC20lb"))
)
first_result.click()
