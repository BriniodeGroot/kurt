import properties
import time
from selenium import webdriver
from selenium import *

from selenium import webdriver

url = "https://kuleuven.be/kurtqr?id=" + properties.id

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.get(url)
driver.refresh()

inputUsername = driver.find_element("id","username")
inputUsername.send_keys(properties.username)

inputPassword = driver.find_element("id","password")
inputPassword.send_keys(properties.password)

driver.find_element("id","pwdLoginBtn").click()

driver.get(url)
driver.refresh()

time.sleep(10)
driver.close()