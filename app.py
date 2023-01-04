from database import *
from tkinter import *


'''
Instructions:
    
    1) save all files (User.py, app.py, database.py, login_details.sqlite) inside the same folder
    2) always run app.py
    

'''

# create window

root = Tk()
root.geometry("300x400")

LOGIN = Label(root, text = 'LOGIN', font=("Helvetica", 16)).pack()

name = Label(root, text = '\nuser name/ email id\n', font=("Helvetica", 16)).pack()

idvar = StringVar()
entry = Entry(root, textvariable = idvar, bg = 'white', fg = 'black').pack()

passw = Label(root, text = '\npassword\n', font=("Helvetica", 16)).pack()

pvar = StringVar()
entry2 = Entry(root, textvariable = pvar, show = '*',bg = 'white', fg = 'black').pack()

text = StringVar()
text.set('')

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

label_valid = Label(root, textvariable = text, fg = 'black', font=("Helvetica", 16)).pack()

button = Button(root, text = "Login", padx = 15 , pady = 5, command = login, fg = 'black', bg = 'white').pack()

button2 = Button(root, text = "Sign up", padx = 15 , pady = 5, command = create_window).pack()


root.mainloop()
 
