import tkinter as tk
from welcome import WelcomePage
from tkinter import messagebox

def main():
    root = tk.Tk()
    
    root.geometry("600x400")
    # Create the welcome page
    welcome_page = WelcomePage(root)
    welcome_page.pack()
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main loop
    root.mainloop()
    

    


if __name__ == "__main__":
    main()
