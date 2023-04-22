#import requests
import time
import json
#from requests_html import HTMLSession
from selenium.webdriver.common.by import By 
#import requests_html
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#import lxml





#setup connection
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

def connect(ip):
    driver.get(ip)

    #frontier specific
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "login-table")))

def login(username, password, force = True):
    #input_box1 = driver.find_element(By.XPATH, "//input[@ng-model='username']")
    input_box2 = driver.find_element(By.XPATH, "//input[@type='password']")
    submit = driver.find_element(By.XPATH, "//button[@ng-click='login()']")
    #input_box1.send_keys("admin")
    input_box2.send_keys(password)

    submit.click()

    if isLoggedIn():
        return True
    if force:
        f = open('logins.json')
        data = json.load(f)

        for credential in data['logins']:
            print(credential)
            print("Trying:")
            print("Username: ", credential["user"])
            print("Password: ", credential["pass"])
            if isLoggedIn():
                return True
        return False

    

#page_source = driver.page_source

def isLoggedIn():
    print("checking login status", end = "")
    for i in range(0, 3):
        print('.', end = "")
        time.sleep(1)
    print()
    try:
        driver.find_element(By.CLASS_NAME, "header")
        print("login failed")
        return False
    except:
        try:
            driver.find_element(By.ID, "wireless_tab")
            print("Login Succeeded")
            return True
        except:
            print("login failed")
            return False
    


#configure test username and password
# username = 'admin'
# password = '(2*b)||!(2*b)==TRUE'
# ip = "192.168.1.1"
# ip = "http://" + ip


# connect(ip)
# login(username, password)
# time.sleep(2)
# thing = isLoggedIn()
# print(thing)
#print(driver.page_source)