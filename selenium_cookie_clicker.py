from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\smester 3\salenium/chromedriver.exe")
driver.get("http://orteil.dashnet.org/experiments/cookie/")
data = driver.find_element(by=By.ID, value="cookie")
# clickes for 60 secs
timeout = time.time() + 60
while True:
    test = 0
    if test == 5 or timeout < time.time():
        count = driver.find_element(by=By.ID,value="money")
        print(f"cookie clicked count = {count.text}")
        break;
    else:
        data.click()
        test += 1
