import tkinter as tk

class InsecurePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create the welcome label
        welcome_label = tk.Label(self, text="Your router is insecure!", font=("Aerial", 20))
        welcome_label.pack(pady=10)
        # Create the next button
        next_button = tk.Button(self, text="Next", font=("Aerial", 12), command=self.go_to_next_page)
        next_button.pack(pady=10)
        
    def go_to_next_page(self):
        self.show_next_page()

    def show_next_page(self):
        # Remove the welcome page from the root window
        #TRY TO MAKE THIS A FOR LOOP
        for slave in self.master.pack_slaves():
            slave.pack_forget()
        # welcome_page = self.master.pack_slaves()[0]
        # welcome_page.pack_forget()
        
        # Create the next page and add it to the root window
        # next_page = MenuPage(self.master)
        # next_page.pack()