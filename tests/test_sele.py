from selenium import webdriver


driver = webdriver.Chrome(
    r"C:\Users\NITHIN G\Downloads\chromedriver-win64_1\chromedriver-win64\chromedriver.exe"
)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")