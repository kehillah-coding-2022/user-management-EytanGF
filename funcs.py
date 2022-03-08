import hashlib


def open_file(filename, mode):
    myFile = open(filename, mode)
    return myFile

def close_file(filename):
    close(filename)

def startmenu():
    print("Hi, welcome to user management. Press enter to begin.")
    input()
    print("Would you like to:")
    print('1) register')
    print('2) login')
    print('3) exit')
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
    print("You are now registered. Would you like to:")
    print("1) login to your account")
    print('2) exit')
    resp = input()
    return resp

def unsuccessful_login():
    print("Username not found. Choose an option:")
    print("1) try logging in again")
    print("2) register an account")
    print("3) exit")
    resp = input()
    return resp

def login_true_msg():
    if login() == True:
        print("You are now logged in. Welcome.")
        birthday_menu()

def birthday_menu():
        print("")
        print('Please choose an option by typing the corresponding number and pressing enter:')
        print("1) add/edit birthday")
        print('2) view birthday')
        print("3) exit")
        resp = int(input())
        if resp == 1:
            add_edit_birthday()
        if resp == 2:
            view_birthday()
        if resp == 3:
            exit()

def add_edit_birthday():
    birthdays = open_file('birthdays.txt', 'r')
    birthdays_list = birthdays.readlines()
    birthdays.close()
    print("Please enter what you want your birthday to be saved as in MM/DD/YYYY format")
    birthday = str(input())
    birthdays1 = open_file('birthdays.txt', 'w')
    birthdays_list[i-1] = (birthday + '\n')
    birthdays1.writelines(birthdays_list)
    birthdays1.close()
    print("Thank you")
    print("")
    print("Please select an option:")
    print("1) Go back to main menu")
    print("2) Go to birthday menu")
    print("3) Exit")
    resp = int(input())
    if resp == 1:
        main()
    if resp == 2:
        birthday_menu()
    if resp == 3:
        exit()

def view_birthday():
    birthdays = open_file('birthdays.txt', 'r')
    birthdays_list = birthdays.readlines()
    birthdays.close()
    if birthdays_list[i-1] == 'a\n':
        print("Sorry, you haven't created a username yet.")
        birthday_menu()
    else:
        print('Your birthday is: ' + birthdays_list[i-1])
        print("")
        print("Please select an option:")
        print("1) Go back to main menu")
        print("2) Go to birthday menu")
        print("3) Exit")
        resp = int(input())
        if resp == 1:
            main()
        if resp == 2:
            birthday_menu()
        if resp == 3:
            exit()






def username_occur(username):
    usernames = open_file('usernames.txt', 'r')
    i = 1
    for line in usernames:
        if username == line.strip():
            break
        i = i + 1
    return i

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
    if int(resp) == 3:
        exit()



def register():
    usernames = open_file('usernames.txt', 'a')
    passwords = open_file('passwords.txt', 'a')
    birthdays = open_file('birthdays.txt', 'a+')
    username = username_create()
    password = password_create()
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    usernames.write('{0}'.format(username + '\n'))
    passwords.write('{0}'.format(hash + '\n'))
    data = birthdays.read()
    # if len(data) > 0:
    #     birthdays.write('{0}'.format('\n' + 'a\n'))
    #     counter = counter + 1
    # else:
    #     birthdays.write('{0}'.format('a\n'))
    birthdays.write('{0}'.format('a\n'))
    usernames.close()
    passwords.close()
    birthdays.close()
    return True

def login():
    print("Please enter your username, case sensitive")
    username = input()
    usernames = open_file('usernames.txt', 'r')
    passwords = open_file('passwords.txt', 'r')
    global i
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
        hash = hashlib.md5(password.encode('utf-8')).hexdigest()
        global j
        j = 1
        for pline in passwords:
            if j == i:
                sought_password = pline.strip()
                break
            j = j + 1

        if hash == sought_password:
            return True
        else:
            print('Incorrect password, please try again.')
            password = input()
            logged_in = password_loop(password, sought_password)
            return logged_in

    else:
        resp = unsuccessful_login()
        if int(resp) == 1:
            login_true_msg()
        elif int(resp) == 2:
            if register() == True:
                resp = after_register()
                if int(resp) == 1:
                    login_true_msg()
                elif int(resp) == 2:
                    exit()
        elif int(resp) == 3:
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
