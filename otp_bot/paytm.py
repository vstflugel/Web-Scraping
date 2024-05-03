from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

# Creating the chrome instance 
driver = webdriver.Chrome()

driver.get("https://aa.phonepe.com/client/")

element = driver.find_element(By.XPATH, "//input[@class='MobileNoInput_mobileInput__UOWiC']")

element.send_keys("7294138044", Keys.RETURN)
driver.implicitly_wait(15)
time.sleep(10)
