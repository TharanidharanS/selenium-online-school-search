from selenium import webdriver
from selenium.webdriver.common.by import By
driver =webdriver.Chrome(executable_path="C:/Users/tharun/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
driver.find_element(by=By.NAME,value="userName").send_keys("admin")
driver.find_element(by=By.NAME,value="password").send_keys("admin")
driver.find_element(by=By.NAME,value="submit").click()
driver.close()