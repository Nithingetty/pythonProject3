#we need to install request package through file-->Settings ---->projectinterpreter
import time

from playwright.sync_api import expect

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests as requests
from selenium.webdriver.support.expected_conditions import none_of

driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/select/single_select")

Choose_language=Select(driver.find_element(By.XPATH,"//select[@id='id_choose_language']"))

Choose_language.select_by_visible_text("Python")
Choose_language.select_by_value("4")
Choose_language.select_by_index(2)
time.sleep(5)