import time
import datetime
import properties
from selenium import webdriver
from selenium import *
from selenium import webdriver

d = datetime.datetime.now()
day = int(d.strftime("%d")) + 8

url = "https://www-sso.groupware.kuleuven.be/sites/KURT/Pages/NEW-Reservation.aspx?StartDateTime=2023-01-" + str(day) + "T09:00:00&EndDateTime=2023-01-" + str(day)+ "T17:00:00&ID=" + properties.id + "&type=b&sessionId=4ee29df8-8343-4be5-a5b4-7985c1ad151f"

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

checkboxAgree = driver.find_element("xpath",'//*[@id="complyConditionsCheckbox"]')
driver.execute_script("arguments[0].click();", checkboxAgree)

submitBtn = driver.find_element("xpath", '//*[@id="submitReservationButton"]')
driver.execute_script("arguments[0].click();", submitBtn)

time.sleep(10)
driver.close()