import tkinter as tk

class SecurePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create the welcome label
        label = tk.Label(self, text="Your router is secure!", font=("Aerial", 20))
        label.pack(pady=10)
        