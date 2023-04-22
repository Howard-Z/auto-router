import requests
import time
from requests_html import HTMLSession
from selenium.webdriver.common.by import By 
import requests_html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import lxml


#configure test username and password
username = 'admin'
password = '(2*b)||!(2*b)==TRUE'
ip = "192.168.1.1"
ip = "http://" + ip


#setup connection
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(ip)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "login-table")))

#input_box1 = driver.find_element(By.XPATH, "//input[@ng-model='username']")
input_box2 = driver.find_element(By.XPATH, "//input[@type='password']")

submit = driver.find_element(By.XPATH, "//button[@ng-click='login()']")
#input_box1.send_keys("admin")
input_box2.send_keys("(2*b)||!(2*b)==TRUE")

submit.click()


page_source = driver.page_source


#content = driver.find_element(By.ID, "login-table")
print(page_source)