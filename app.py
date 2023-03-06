from database import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import Font

'''
Instructions:
    
    1) save all files (User.py, app.py, database.py, login_details.sqlite) inside the same folder
    2) always run app.py
    

'''

# create window



root = tk.Tk()
root.geometry("300x400")
root.title("Login")



entries_frame = tk.Frame(root)


LOGIN = tk.Label(root, text = 'LOGIN', font=("Segoi UI", 16))

name = tk.Label(root, text = '\nuser name/ email id\n', font=("Helvetica", 16)).pack()

idvar = tk.StringVar()
entry = ttk.Entry(root, textvariable = idvar).pack()

passw = tk.Label(root, text = '\npassword\n', font=("Helvetica", 16)).pack()

pvar = tk.StringVar()
entry2 = ttk.Entry(root, textvariable = pvar, show = '*').pack()

text = tk.StringVar()
passw = tk.Label(root, textvariable= text, font=("Helvetica", 16)).pack()


# clear entry fields
def clear():
    idvar.set('')
    pvar.set('')

# change label text
def change(txt):
    text.set(txt)


# button command (Sign-up)
def create_window():
    root.destroy()
    import signup

   
# Button command (login)

def login():
    usid = idvar.get()
    pss = pvar.get()
    
    if len((usid).strip()) == 0 or len(pss.strip()) == 0:
        change('\nall fields are required\n')
        empty = True
    else:
        empty = False

    if not empty: 
        exists = verify(str(usid), str(pss))
        if exists[0] == False:
            clear()
            change('Account does not exist please sign up')
        else:
            if exists[1] == False:
                clear()
                change('Incorrect password')
            else:
                change('Login successful')
                print('Process completed successfully')



button = ttk.Button(root, text = "Login", command = login).pack()

button2 = ttk.Button(root, text = "Sign up", command = create_window).pack(pady=5)


root.mainloop()
 
