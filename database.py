import sqlite3

# connect to file
conn = sqlite3.connect('login_details.sqlite')
# create cursor
cur = conn.cursor()

# create database record
def create(uid, email, password):
    exists = False
    rename = False
    sqlcheck = 'SELECT username, email FROM Login'
    for row in cur.execute(sqlcheck):
        if str(row[0]) == uid:   
            rename = True
            print('username taken')
            
        if str(row[1]) == email:
            exists = True
            print('account already exists')

        if exists or rename:
            return exists, rename
            break
        
        
    if not exists and not rename:
        cur.execute('''INSERT INTO Login (username, email, password) VALUES (?, ?, ?);''',(uid, email, password))
        conn.commit()


# check if record already exists
def verify(info, passw):
    userinfo = False
    password = False 
    sqlcheck = 'SELECT username, email, password FROM Login'
    for row in cur.execute(sqlcheck):
        if info == row[0] or info == row[1]:
            userinfo = True
            if passw == row[2]:
                password = True
                return userinfo, password
                break
    return userinfo, password


    

