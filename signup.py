import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import database
import re

# create window

master = tk.Tk()

FONT_1 = Font(family='Segoe UI', 
              size=13, 
              weight='bold'
              )

FONT_2 = Font(family='Segoe UI', 
              size=8, 
              weight='bold'
              )

FONT_3 = Font(family='Segoe UI', 
              size=15, 
              weight='bold'
              )

signup = tk.Label(master, text = 'Sign-up', font=FONT_3).pack(padx=90, pady=20)

slave = tk.Label(master, text = 'Username', font=FONT_1).pack()

uidvar = tk.StringVar()
username = ttk.Entry(master, textvariable = uidvar).pack()

slave2 = tk.Label(master, text = 'Email ID', font=FONT_1).pack()

idvar2 = tk.StringVar()
email = ttk.Entry(master, textvariable = idvar2).pack()

slave3 = tk.Label(master, text = 'Password', font=FONT_1).pack()

def validate_pass(name, index, mode, matchonly=False):
    pss_str = pss.get()
    pss_conf_str = pss2.get()
    if not matchonly:
        CONDITION_1 = '^.*[A-Z].*$'
        CONDITION_2 = '^.*[a-z].*$'
        CONDITION_3 = '^.*[\d].*$'
        CONDITION_4 = '^.*[`~!@#$%^&*()_+|\{\}\[\]\(\)<>;:\'\"\\|].*$'
        CONDITION_5 = '^.{8,}$'
        

        if re.match(CONDITION_1, pss_str):
            r1_lab.config(fg="green")
        else:
            r1_lab.config(fg="red")
        
        if re.match(CONDITION_2, pss_str):
            r2_lab.config(fg="green")
        else:
            r2_lab.config(fg="red")
        
        if re.match(CONDITION_3, pss_str):
            r3_lab.config(fg="green")
        else:
            r3_lab.config(fg="red")

        if re.match(CONDITION_4, pss_str):
            r4_lab.config(fg="green")
        else:
            r4_lab.config(fg="red")
        
        if re.match(CONDITION_5, pss_str):
            r5_lab.config(fg="green")
        else:
            r5_lab.config(fg="red")
        
    if pss_str == pss_conf_str:
        r6_lab.config(fg="green")
    else:
        r6_lab.config(fg="red")
pss = tk.StringVar()
password = ttk.Entry(master, textvariable = pss, show = '*').pack()
pss.trace_add('write', validate_pass)

slave4 = tk.Label(master, text = 'Confirm Password', font=FONT_1).pack()

pss2 = tk.StringVar()
passcheck = ttk.Entry(master, textvariable = pss2, show = '*').pack()
pss2.trace_add('write', lambda x,y,z:validate_pass(x,y,z,matchonly=True))

infovar = tk.StringVar()
notify = tk.Label(master, textvariable = infovar , font=FONT_1).pack()

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

    PASSWORD_VALID_CONDITION = '^(?=.*[A-Z].*)(?=.*[\d].*)(?=.*[a-z].*)(?=.*[`~!,@#$%^&*()_+|\{\}\[\]\(\)<>;:\'\"\\|].*).{8,}$'
    EMAIL_VALID_CONDITION = '^[^\.].*[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~].*[^\.]@.*[A-Za-z0-9\-][\.]{1, 100}$'

    if len(usrid.strip()) < 1 or len(emlid.strip()) < 1 or len(psswrd.strip()) < 1 or len(check.strip()) < 1:
        change_label('all fields required')
        ok = False
    
    elif not re.match(PASSWORD_VALID_CONDITION, psswrd):
        change_label('password does not meet criteria')
        pss.set('')
        pss2.set('')
        ok = False
    
    elif not re.match(EMAIL_VALID_CONDITION, emlid):
        change_label('invalid email')
        idvar2.set('')
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


validate_frame = tk.Frame(border=5)

r1_lab =tk.Label(validate_frame, text="• contains at least one uppercase ", fg="red", font=FONT_2)
r1_lab.pack()
r2_lab =tk.Label(validate_frame, text="• contains at least one lowercase", fg="red", font=FONT_2)
r2_lab.pack()
r3_lab =tk.Label(validate_frame, text="• contains at least one digit", fg="red", font=FONT_2)
r3_lab.pack()
r4_lab =tk.Label(validate_frame, text="• contains at least one special character", fg="red", font=FONT_2)
r4_lab.pack()
r5_lab =tk.Label(validate_frame, text="• contains minimum of 8 chracters", fg="red", font=FONT_2)
r5_lab.pack()
r6_lab =tk.Label(validate_frame, text="• passwords match", fg="red", font=FONT_2)
r6_lab.pack()
validate_frame.pack()
but = ttk.Button(master, text = 'sign-up', command = create_acc).pack()

# button command
def return_to_login():
    master.destroy()
    import app


but2 = ttk.Button(master, text = 'login', command = return_to_login).pack()




master.mainloop()
