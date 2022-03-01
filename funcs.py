
def open_file(filename, mode):
    myFile = open(filename, mode)
    return myFile

def close_file(filename):
    close(filename)

def startmenu():
    print("Hi, welcome to user management. Press enter to begin.")
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

def check_password(entered_password):
    passwords = open_file('passwords.txt', 'r')
    for line in passwords:
        if entered_password == line.strip():
            print("Sorry, that password is already taken. Please enter a different password")
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
    print("Please enter an 8 or more character password")
    password = input()
    while len(password) < 8:
        print("Sorry, you password needs to be at least 8 characters. Please reenter a password.")
        password = input()
    status = False
    while status == False:
        status = check_password(password)
        if status == False:
            password = input()
        else:
            status = True
    return password

def after_register():
    print("You are now registered. Would you like to 1) login to your account or 2) exit")
    resp = input()
    return resp

def unsuccessful_login():
    print("Username not found. Please 1) register or 2) exit")
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
    usernames.close()
    passwords.close()
    return True

def login():
    print("Please enter your username, case sensitive")
    username = input()
    usernames = open_file('usernames.txt', 'r')
    passwords = open_file('passwords.txt', 'r')
    i = 1
    username_matched = False
    for line in usernames:
        if username == line.strip():
            username_matched = True
            break
        i = i + 1
    if username_matched == True:
        print('Please enter your password, case sensitive')
        password = input()
        j = 1
        for pline in passwords:
            if j == i:
                sought_password = pline.strip()
                break
            j = j + 1

        if password == sought_password:
            return True
        else:
            print('Incorrect password, please try again.')
            password = input()
            logged_in = password_loop(password, sought_password)
            return logged_in

    else:
        resp = unsuccessful_login()
        if int(resp) == 1:
            if register() == True:
                resp = after_register()
                if int(resp) == 1:
                    login_true_msg()
                elif int(resp) == 2:
                    exit()
        if int(resp) == 2:
            exit()

    return False


def password_loop(password, sought_password):
    attempts = 3
    while attempts > 0:
        if password == sought_password:
            return True
        print('Incorrect password, please try again.')
        password = input()
        attempts = attempts - 1
    print('Maximum password attemps reached. Sorry.')
    return False
