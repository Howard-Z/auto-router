#import requests
import time
import json
import tkinter as tk
#from requests_html import HTMLSession
from selenium.webdriver.common.by import By 
#import requests_html
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from insecure import InsecurePage
from secure import SecurePage
#import lxml

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        #self.master = master
        
        # Create the next page label
        main_text = "Click to start running the program"
        next_page_label = tk.Label(master, text=main_text)
        next_page_label.pack(pady=10)

        #setup connection
        
        
        #Create the next button
        next_button = tk.Button(self, text="Start", font=("Aerial", 12), command=self.start)
        next_button.pack(pady=10)
        
        
    def start(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.connect("http://192.168.1.1")
        if self.login("", ""):
            self.show_next_page(True)
        else:
            self.show_next_page(False)


    def show_next_page(self, insecure):
        # Remove the welcome page from the root window
        for slave in self.master.pack_slaves():
            slave.pack_forget()
        # welcome_page = self.master.pack_slaves()[0]
        # welcome_page.pack_forget()
        
        # Create the next page and add it to the root window
        if insecure:
            next_page = InsecurePage(self.master)
        else:
            next_page = SecurePage(self.master)
        next_page.pack()

    

    def connect(self, ip):
        self.driver.get(ip)

        #frontier specific
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "login-table")))

    def login(self, username, password, force = True):
        if self.login_attempt(username, password):
            return True
        if force:
            f = open('logins.json')
            data = json.load(f)
            for credential in data['logins']:
                if self.login_attempt(credential["user"], credential["pass"]):
                    return True
            return False
        return False


    def login_attempt(self, username, password, debug = False):
        if debug:
            print("Trying:")
            print("Username: ", username)
            print("Password: ", password)

        input_box2 = self.driver.find_element(By.XPATH, "//input[@type='password']")
        input_box2.send_keys(password)

        submit = self.driver.find_element(By.XPATH, "//button[@ng-click='login()']")
        submit.click()
        if self.isLoggedIn():
            return True
        return False


    def isLoggedIn(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.CLASS_NAME, "header")
            return False
        except:
            try:
                self.driver.find_element(By.ID, "wireless_tab")
                return True
            except:
                return False




        
