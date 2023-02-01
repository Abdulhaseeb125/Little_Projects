from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "E:\smester 3\salenium\chromedriver.exe"
data_list = []
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.python.org/")
dates = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget .menu time')
date_list = [item.text for item in dates]
content = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget .menu li a')
content_list = [item.text for item in content]
content = {}
for n in range(len(date_list)):
    content[n] = {
        'time': date_list[n],
        'name': content_list[n]
    }

print(content)

driver.quit()
