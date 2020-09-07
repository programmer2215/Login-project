class User:
    def __init__(self, username, emailid, password):
        self.username = username
        self.emailid = emailid
        self.password = password

    def validpass(self, password):
        if self.password == password:
            return True
        else:
            return False

    
