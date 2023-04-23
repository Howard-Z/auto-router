#import requests
import time
import json
from django.shortcuts import render
from django.http import StreamingHttpResponse
import os
import subprocess
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = None
driver = None
ip = "http://192.168.1.1"
passwd = ""
usern = ""

def start():
    global options
    global driver
    global ip
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    connect(ip)
    return login("admin", "1234") #needs to be replaced

def connect(ip):
    global driver

    driver.get(ip)

    #frontier specific
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "login-table")))

def login(username, password, force = True):
    global usern
    global passwd
    output = ""
    output += login_attempt(username, password)
    if isLoggedIn():
        password = password
        usern = username
        return output, True, username, password
    if force:
        f = open(os.getcwd() + "\logins.json")
        data = json.load(f)
        for credential in data['logins']:
            output += login_attempt(credential["user"], credential["pass"])
            if isLoggedIn():
                usern = credential["user"]
                passwd = credential["pass"]
                return output, True, credential["user"], credential ["pass"]
        return output, False, "", ""
    return output, False, "", ""


def login_attempt(username, password, debug = False):
    global driver

    if debug:
        print("Tried:")
        print("Username: ", username)
        print("Password: ", password)
    input_box2 = driver.find_element(By.XPATH, "//input[@type='password']")
    input_box2.send_keys(password)

    submit = driver.find_element(By.XPATH, "//button[@ng-click='login()']")
    submit.click()
    return "Tried: { Username: " + str(username) + ", Password: " + str(password) + "}\n"
    # if isLoggedIn():
    #     return True
    # return False


def isLoggedIn():
    global driver
    time.sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, "header")
        return False
    except:
        try:
            driver.find_element(By.ID, "wireless_tab")
            return True
        except:
            return False


def login_render(request):
    if request.method == 'POST':
        output, status, username, password = start()
        output = output.split('\n')
        output = output[0:-1:1]
        if isLoggedIn():
            return render(request, 'login.html', {'results': output, 'showbtn' : False, 'secure' : status, "username" : username, "password" : password})
        else:
            return secure(request)
    else:
        return render(request, 'login.html', {'showbtn' : True})

def fixme(request):
    global driver
    global options
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    connect(ip)
    login(usern, passwd)
    if isLoggedIn():
        driver.get("http://192.168.1.1/#/advanced/users?edit=true&frommain=true")
    return render(request, 'fixme.html')


def secure(request):
    return render(request, 'secure.html')