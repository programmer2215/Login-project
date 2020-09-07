from tkinter import *
import database

# create window

master = Tk()
master.geometry('400x400')

signup = Label(master, text = 'Sign-up', font=("Helvetica", 16)).pack()

slave = Label(master, text = 'enter a username', font=("Helvetica", 16)).pack()

uidvar = StringVar()
username = Entry(master, textvariable = uidvar).pack()

slave2 = Label(master, text = 'enter an email ID', font=("Helvetica", 16)).pack()

idvar2 = StringVar()
email = Entry(master, textvariable = idvar2).pack()

slave3 = Label(master, text = 'enter a password', font=("Helvetica", 16)).pack()

pss = StringVar()
password = Entry(master, textvariable = pss, show = '*').pack()

slave4 = Label(master, text = 're-enter the password', font=("Helvetica", 16)).pack()

pss2 = StringVar()
passcheck = Entry(master, textvariable = pss2, show = '*').pack()

infovar = StringVar()
notify = Label(master, textvariable = infovar , font=("Helvetica", 16)).pack()

# change label text 
def change_label(txt):
    infovar.set(txt)

# clear entry field
def cls():
    uidvar.set('')
    idvar2.set('')
    pss.set('')
    pss2.set('')

# validate entry fields and create "account"
def create_acc():
    ok = True
    usrid = uidvar.get()
    emlid = idvar2.get()
    psswrd = pss.get()
    check = pss2.get()

    if len(usrid.strip()) < 1 or len(emlid.strip()) < 1 or len(psswrd.strip()) < 1 or len(check.strip()) < 1:
        change_label('all fields required')
        ok = False

    elif len(psswrd) < 6:
        change_label('password must atleast be 6 chars long')
        pss.set('')
        pss2.set('')
        ok = False

    elif psswrd != check:
        change_label('password does not match')
        pss.set('')
        pss2.set('')
        ok = False

    if ok:
        a = database.create(usrid, emlid, psswrd)
        if a != None:
            if a[1] == True:
                change_label('Username already taken')
                cls()
            elif a[0] == True:
                change_label('Account already exists')
                cls()
        else:
            cls()
            change_label('account created successfully')
    print(ok)

but = Button(master, text = 'sign-up', command = create_acc).pack()

# button command
def return_to_login():
    master.destroy()
    import app


but2 = Button(master, text = 'login', command = return_to_login).pack()

master.mainloop()







