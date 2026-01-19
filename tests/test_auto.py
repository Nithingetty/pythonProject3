import time

from playwright.sync_api import sync_playwright

def test_search_and_add_asus_laptop_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        
        page.frame()
        
        
        
        
        time.sleep(10)

     
 