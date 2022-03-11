import hashlib
import random
import smtplib, ssl


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
            print("Sorry, that email is already taken. Please enter a different username")
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
    print("Email not found. Choose an option:")
    print("1) try logging in again")
    print("2) register an account")
    print("3) exit")
    resp = input()
    return resp

def login_true_msg():
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
    usernames = open_file('usernames.txt', 'a')
    passwords = open_file('passwords.txt', 'a')
    birthdays = open_file('birthdays.txt', 'a+')
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
    resp = int(input)
    if resp == 1:
        main()
    if resp == 2:
        exit()




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
    codes = open_file('recoverycodes.txt', 'a')
    username = username_create()
    password = password_create()
    usernames.write('{0}'.format(username + '\n'))
    passwords.write('{0}'.format(hash + '\n'))
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
    code_verified = False
    attempts = 3
    while attempts > 0 and code_verified == False:
        if str(code_input) == str(msg):
            code_verified = True
            print('Verified')
            print('')
            print('Working...')
            print('')
        elif attempts == 0:
            print('Maximum password attemps reached. Sorry.')
            exit()
        else:
            print('Incorrect recovery code, please try again.')
            password = input()
            attempts = attempts - 1


def reset_email_password():
    print('Please enter your recovery code')
    code = input()
    if code_input_loop(code) == True:
        pass
    emails = open_file('usernames.txt', 'r')
    passwords = open_file('passwords.txt', 'r')
    emails_list = emails.readlines()
    passwords_list = passwords.readlines()
    emails.close()
    passwords.close()
    print("Please enter your new email")
    email = str(input())
    emails1 = open_file('emails.txt', 'w')
    emails_list[i-1] = (email + '\n')
    emails1.writelines(emails_list)
    emails1.close()
    print("Please enter your new password")
    password = str(input())
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    passwords1 = open_file('passwords.txt', 'w')
    passwords_list[z-1] = (hash + '\n')
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
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def login():
    print('If you forgot your email or password, press 1. Else, press 2.')
    resp = int(input())
    if resp == 1:
        print("Please enter the email that you want to send this recovery to")
        email = input()
        global msg
        msg = code_create(6)
        print(msg)
        str_msg = str(msg)
        if emailsend(email, 'pythonacctrecov@gmail.com', 'password1234!', 'Account Recovery Code', str_msg) == True:
            reset_email_password()
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
    attempts = 3
    while attempts > 0:
        if password == sought_password:
            return True
        print('Incorrect password, please try again.')
        password = input()
        attempts = attempts - 1
    print('Maximum password attemps reached. Sorry.')
    return False
