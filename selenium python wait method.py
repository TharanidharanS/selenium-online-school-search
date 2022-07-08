import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# set the path of the browser or chrome driver
driver =webdriver.Chrome(executable_path="C:/Users/tharun/Downloads/chromedriver_win32/chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/index.php")

# adding page load timeout
#driver.set_page_load_timeout(30)

# add implicit wait method
driver.implicitly_wait(10)

driver.find_element(by=By.NAME,value="userName").send_keys("admin")

# add time.sleep
time.sleep(30)

driver.find_element(by=By.NAME,value="password").send_keys("admin")

# add explicit wait method
#element = WebDriverWait(driver,50).until(EC.presence_of_element_located(By.NAME,"submit"))

#driver.find_element(by=By.NAME,value="submit").click()


