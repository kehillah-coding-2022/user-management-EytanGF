
def open_file(filename, mode):
    myFile = open(filename, mode)
    return myFile

def close_file(filename):
    close(filename)

def startmenu():
    print("Hi, welcome to user management")
    input()
    print("Would you like to 1) register or 2) login")
    resp = input()
    return resp

def check_username(entered_username):
    usernames = open_file('usernames.txt', 'r')
    for line in usernames:
        if entered_username == line.strip():
            print("Sorry, that username is already taken. Please enter a different username")
            return False
        else:
            return True

def username_create():
    usernames = open_file('usernames.txt', 'r')
    print("Please enter a username")
    username = input()
    status = False
    while status == False:
        status = check_username(username)
        if status == False:
            username = input()
        else:
            status = True
    return username

def password_create():
    print("Please enter a password")
    password = input()
    while len(password) < 8:
        print("Sorry, you password needs to be at least 8 characters. Please reenter a password.")
        password = input()
    return password

def after_register():
    print("You are now registered. Would you like to 1) losgin to your account or 2) exit")
    resp = input()
    return resp

def login_true_msg():
        if login() == True:
            print("You are now logged in. Welcome")


def main():
    resp = startmenu()
    if int(resp) == 1:
        if register() == True:
            resp = after_register()
            if int(resp) == 1:
                login_true_msg()
            elif int(resp) == 2:
                exit()
    if int(resp) == 2:
        login_true_msg()


def register():
    usernames = open_file('usernames.txt', 'a')
    passwords = open_file('passwords.txt', 'a')
    username = username_create()
    password = password_create()
    usernames.write('{0}'.format(username + '\n'))
    passwords.write('{0}'.format(password + '\n'))
    return True

def login():
    print("Please enter a username, case sensitive")
    username = input()
    usernames = open_file('usernames.txt', 'r')
    # for line in usernames:
    #     if username == line:
    #         ""
