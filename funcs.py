import hashlib
import random
import smtplib, ssl


def open_file(filename, mode):
    """
    Given a filename and a desired mode to open it in, open that file in that mode
    """
    myFile = open(filename, mode)
    return myFile

def close_file(filename):
    """
    given a file, close that file
    """
    close(filename)

def startmenu():
    """
    give user 3 options for first experience
    """
    print("Hi, welcome to user management. Press enter to begin.")
    input()
    print("Would you like to:")
    print('1) register')
    print('2) login')
    print('3) exit')
    resp = input()
    return resp

def check_username(entered_username):
    """
    given a username inputted by the user, check if that username is already taken
    """
    usernames = open_file('usernames.txt', 'r')
    for line in usernames:
        if entered_username == line.strip():
            print("Sorry, that email is already taken. Please enter a different username")
            return False
        else:
            return True

def check_password(entered_password):
    '''
    given a password entered by the user, check if that password is already taken
    '''
    passwords = open_file('passwords.txt', 'r')
    for line in passwords:
        if entered_password == line.strip():
            print("Sorry, that password is already taken. Please enter a different password")
            return False
    else:
        return True

def username_create():
    """
    create and return username, call check username function to check that username is unique
    """
    usernames = open_file('usernames.txt', 'r')
    print("Please enter an email")
    username1 = input()
    status = False
    while status == False:
        status = check_username(username1)
        if status == False:
            username1 = input()
        else:
            status = True
    return username1

def password_create():
    """
    create and return password, call check password function to check that password is unique
    """
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
    hashed = hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hashed

def after_register():
    '''
    user menu that activates after a user has registered an account
    '''
    print("You are now registered. Would you like to:")
    print("1) login to your account")
    print('2) exit')
    resp = input()
    return resp

def unsuccessful_login():
    '''
    give user menu if their email wasn't found in the system
    '''
    print("Email not found. Choose an option:")
    print("1) try logging in again")
    print("2) register an account")
    print("3) exit")
    resp = input()
    return resp

def login_true_msg():
    '''
    after-successful-login menu
    '''
    if login() == True:
        print('')
        print("You are now logged in. Welcome.")
        print('')
        print('Select an option')
        print('1) birthday menu')
        print('2) delete your account')
        print('3) exit')
        resp = int(input())
        if resp == 1:
            birthday_menu()
        if resp == 2:
            delete_account()
        if resp == 3:
            exit()


def delete_account():
    '''
    delete a user's account and all of their stored data
    '''
    delete_true = False
    while delete_true == False:
        print('')
        print("To delete your account please type in 'delete', case sensitive")
        resp = str(input())
        if resp == 'delete':
            delete_true = True
        else:
            print('Please try again')

    usernames = open_file('usernames.txt', 'r')
    passwords = open_file('passwords.txt', 'r')
    birthdays = open_file('birthdays.txt', 'r')
    usernames_list = usernames.readlines()
    passwords_list = passwords.readlines()
    birthdays_list = birthdays.readlines()
    usernames.close()
    passwords.close()
    birthdays.close()
    usernames = open_file('usernames.txt', 'w')
    passwords = open_file('passwords.txt', 'w')
    birthdays = open_file('birthdays.txt', 'w')
    del birthdays_list[i-1]
    del passwords_list[i-1]
    del usernames_list[i-1]
    usernames.writelines(usernames_list)
    passwords.writelines(passwords_list)
    birthdays.writelines(birthdays_list)
    usernames.close()
    passwords.close()
    birthdays.close()
    print("")
    print('Your account has been deleted.')
    print('')
    print('Please select an option:')
    print('1) Main menu')
    print('2) Exit')
    resp = int(input())
    if resp == 1:
        main()
    if resp == 2:
        exit()




def birthday_menu():
    '''
    give user birthday menu options and interactive ability
    '''
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
    '''
    add/edit user's birthday
    '''
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
    '''
    let user view birthday
    '''
    birthdays = open_file('birthdays.txt', 'r')
    birthdays_list = birthdays.readlines()
    birthdays.close()
    if birthdays_list[i-1] == 'a\n':
        print("Sorry, you haven't entered a birthday yet.")
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
    '''
    check if username is unique
    '''
    usernames = open_file('usernames.txt', 'r')
    i = 1
    for line in usernames:
        if username == line.strip():
            break
        i = i + 1
    return i

def main():
    '''
    main function
    '''
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
    '''
    register a user
    '''
    usernames = open_file('usernames.txt', 'a')
    passwords = open_file('passwords.txt', 'a')
    birthdays = open_file('birthdays.txt', 'a+')
    username = username_create()
    password = password_create()
    usernames.write('{0}'.format(username + '\n'))
    passwords.write('{0}'.format(password + '\n'))
    birthdays.write('{0}'.format('a\n'))
    usernames.close()
    passwords.close()
    birthdays.close()
    return True


def emailsend(receiver_email, sender_email, password, subject, msg):
    """
    given the receivers email, password, subject, and message, send an email to the receiver.
    """
    email_sent = False
    smtp_server = "smtp.gmail.com"
    messagebody = ("Your recovery code is " + (msg))
    message = 'Subject: {}\n\n{}'.format(subject, messagebody)
    port = 587
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        email_sent = True
    return email_sent

def code_input_loop(code_input):
    '''
    given an inputted verification code to recover an account, make sure that they only have 3 chances
    '''
    attempts = 3
    while attempts > 0:
        if str(code_input) == str(msg):
            print('Verified')
            print('')
            print('Working...')
            print('')
            return True
        elif attempts == 0:
            print('Maximum password attemps reached. Sorry.')
            return Falses
            exit()
        print('Incorrect recovery code, please try again.')
        password = input()
        attempts = attempts - 1


def reset_password(email):
    '''
    given a user's email, reset their password
    '''
    print('')
    print('The recovery code has been sent, please check your email.')
    print('')
    print('Please enter your recovery code that was sent to: ' + email)
    code = input()
    if code_input_loop(code) == True:
        pass
    emails = open_file('usernames.txt', 'r')
    passwords = open_file('passwords.txt', 'r')
    passwords_list = passwords.readlines()
    global i
    i = 1
    username_matched = False
    for line in emails:
        if email == line.strip():
            username_matched = True
            break
        i = i + 1
    emails.close()
    passwords.close()
    password = password_create()
    passwords1 = open_file('passwords.txt', 'w')
    passwords_list[i-1] = (password + '\n')
    passwords1.writelines(passwords_list)
    passwords1.close()
    print("Thank you")
    print("")
    print("Please select an option:")
    print("1) Go back to main menu")
    print("2) Exit")
    resp = int(input())
    if resp == 1:
        main()
    if resp == 2:
        exit()


def code_create(n):
    '''
    given n, create a random code with n digits
    '''
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def login():
    '''
    login the user
    '''
    print('If you forgot your password, press 1. Else, press 2.')
    resp = int(input())
    if resp == 1:
        print("Please enter your email")
        email = input()
        global msg
        msg = code_create(6)
        str_msg = str(msg)
        if emailsend(email, 'pythonacctrecov@gmail.com', 'password1234!', 'Account Recovery Code', str_msg) == True:
            reset_password(email)
    if resp == 2:
        pass
    print("Please enter your email, case sensitive")
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
    '''
    given an inputted password and the actual password, make sure that the user only has three tries to input the password, and then the code locks
    '''
    attempts = 3
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    while attempts > 0:
        if hash == sought_password:
            return True
        print('Incorrect password, please try again.')
        password = input()
        hash = hashlib.md5(password.encode('utf-8')).hexdigest()
        attempts = attempts - 1
    print('Maximum password attempts reached. Sorry.')
    return False
