
def open_file_w(filename):
    myFile = open(filename, 'w')
    return myFile

def open_file_r(filename):
    myFile = open(filename, 'r')
    return myFile

def startmenu():
    print("Hi, welcome to user management")
    input()
    print("Would you like to 1) register or 2) login")
    resp = input()
    return resp


def main():
    resp = startmenu()
    register()
    if int(resp) == 1:
        register()
    if int(resp) == 2:
        login()

def register():
    db = open_file_w('userdata.txt')
    print("Please enter a username")
    username = input()
    print("Please enter a password")
    password = input()
    db.write('{0},{1}'.format(username, password))

def login():
    print("Please enter a username, case sensitive")
    username = input()
    db = open_file_r('userdata.txt')
    for line in db:
        if line == username:
            return True
