from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys
import time
sys.path.extend(['login', 'MAC', 'tkinterUI'])
from login import *

root = Tk()
root.geometry("300x200")

# Create a list to store the state of the checkboxes
checkbox_values = [IntVar() for i in range(5)]

# Create a frame to hold the checkboxes
checkbox_frame = Frame(root)
checkbox_frame.pack(side=LEFT)

# Create the checkboxes
checkbox1 = Checkbutton(checkbox_frame, text="Checkbox 1", variable=checkbox_values[0])
checkbox1.pack(anchor=W)
checkbox2 = Checkbutton(checkbox_frame, text="Checkbox 2", variable=checkbox_values[1])
checkbox2.pack(anchor=W)
checkbox3 = Checkbutton(checkbox_frame, text="Checkbox 3", variable=checkbox_values[2])
checkbox3.pack(anchor=W)
checkbox4 = Checkbutton(checkbox_frame, text="Checkbox 4", variable=checkbox_values[3])
checkbox4.pack(anchor=W)
checkbox5 = Checkbutton(checkbox_frame, text="Checkbox 5", variable=checkbox_values[4])
checkbox5.pack(anchor=W)

# Create a frame to hold the file upload button
file_upload_frame = Frame(root)
file_upload_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Function to handle file upload
def open_file_dialog():
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    print(filename)

# Create a button to open the file dialog
upload_button = Button(file_upload_frame, text="Upload File", command=open_file_dialog)
upload_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Function to clear the screen and show the next screen
def show_next_screen():
    # Destroy the existing widgets
    checkbox_frame.destroy()
    file_upload_frame.destroy()
    next_button.destroy()

    # Create a new frame for the next screen
    next_screen_frame = Frame(root)
    next_screen_frame.pack(fill=BOTH, expand=True)

    # # Create two buttons for the next screen
    # yes_button = Button(next_screen_frame, text="Yes")
    # yes_button.pack(side=LEFT, padx=10, pady=10)
    # no_button = Button(next_screen_frame, text="No")
    # no_button.pack(side=LEFT, padx=10, pady=10)

    output = StringVar()
    output_label = Label(root, textvariable=output)
    output_label.pack()
    connect('http://192.168.1.1')

    if (login("admin", "(2*b)||!(2*b)==TRUE")):
        output.set("Login Successful")

    print(thing)  

# Create a button to show the next screen
next_button = Button(root, text="Next", command=show_next_screen)
next_button.pack(side=BOTTOM, pady=5, padx = 10)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
