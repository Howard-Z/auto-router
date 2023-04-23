import tkinter as tk
import time
from login import LoginPage

class MenuPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        #self.master = master
        
        # Create the next page label
        main_text = "This application will now try and log into your router using a short list of common default credentials"
        next_page_label = tk.Label(self, text=main_text)
        next_page_label.pack(pady=10)
        
        # Create the next button
        next_button = tk.Button(self, text="Next", font=("Aerial", 12), command=self.go_to_next_page)
        next_button.pack(pady=10)
        
    def go_to_next_page(self):
        self.show_next_page()

    def show_next_page(self):
        # Remove the welcome page from the root window
        for slave in self.master.pack_slaves():
            slave.pack_forget()
        # welcome_page = self.master.pack_slaves()[0]
        # welcome_page.pack_forget()
        
        # Create the next page and add it to the root window
        next_page = LoginPage(self.master)
        next_page.pack()
        # connect("http://192.168.1.1")
        # login("", "")

