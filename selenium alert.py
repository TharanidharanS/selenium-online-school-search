import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:/Users/tharun/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element(by=By.XPATH,value="//button[contains(text(),'alert box:')]").click()
time.sleep(30)
alertmessage = driver.switch_to.alert.text
print(alertmessage)
driver.switch_to.alert.accept()
driver.find_element(by=By.XPATH,value="//a[contains(text(),'Alert with OK & Cancel')]").click()
driver.find_element(by=By.XPATH,value="//button[contains(text(),'click the button to display a confirm box')]").click()
driver.switch_to.alert.dismiss()
driver.find_element(by=By.XPATH,value="//a[contains(text(),'Alert with Textbox')]").click()
driver.find_element(by=By.XPATH,value="//button[contains(text(),'click the button to demonstrate the prompt box')]").click()


