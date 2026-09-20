users = {}

def ligin_required(func):
    def warpper():
        username = input("username : ")
        password = input("password : ")
        if users.get(username) == password :
            func()
        else:
            print ("wrong username or password")

        return warpper

username = input("register username : ")
password = input("register password : ")

users[username] = password

@login_required
def secret_page():
    print("welcome to secret page")

secret_page()
