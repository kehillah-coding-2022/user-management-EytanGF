# Comprehensive User Management System

## Introduction

This code will allow the user to register an account that saves the email and password of the user. When logged in, the user can add/edit/view their birthday, delete their account and more. If the user forgets their password, this code will send a recovery email with a 6-digit recovery code to the user's email to reset their password.

## Setup

### Downloading `progressbar`

To install the `progressbar` python library, simply run this simple command in your terminal of choice:

#### Windows

```python
python pip install progressbar
```

#### Mac

```python
pip3 install progressbar
```

`hashlib`, `random`, `smtplib`, `ssl`, `time`, and `sys` are all part of the PSL (**P**ython **S**tandard **L**ibrary) so you don't need to download them.

## Functions

Function | Description
------------- | -------------
`main`  | run main code which presents the user with a navigatable menu to begin their user management experience
`register`  | register a user's account; call the `username_create` and `password create` functions
`open_file`  | given a filename and a desired mode to open it in, open that file in that mode
`username_create` | create and return a username; call the `check_username` function to check that the username is unique
`check_username` | given a username inputted by the user, check if that username is already taken
`password_create` | create and return a password; call the `check_password` function to check that the username is unique
`check_password` | given a password inputted by the user, check if that password is already taken
`after_register` | user menu that activates after a user has registered an account
`login true_msg` | calls the `login` function; if `login` is returns `True`, give the user access to the `birthday_menu` and `delete_account` functions, or lets the user exit
`login` | logs the user in
`code_create` | given a number n, create a random code with n digits
`emailsend` | given the receivers email, password, subject, and message, send an email to the receiver and return email_sent status (`True` or `False`)
`reset_password` | given a user's email, reset their password
`code_input_loop` | given an inputted verification code to recover an account, make sure that they only have 3 chances
`password_loop` | given an inputted password and the actual password, make sure that the user only has three tries to input the password, and then the code locks
`unsuccsessful_login` | give user menu if their email wasn't found in the system
`birthday_menu` | give user birthday menu options and interactive ability
`add_edit_birthday` | add/edit a user's birthday
`view_birthday` | let the user view their birthday; if they haven't create a birthday, tell them so
`delete_account` | delete a user's account and all of their stored data
`animated_marker` | activate a loading animation for the user's viewing while the recovery email is sending

## Files

File | File Type | Description | Link
------------- | ------------- | ------------- | -------------
`main` | python (.py) file | Imports the functions file and then calls it | [main.py](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/main.py)
`funcs` | python (.py) file | Runs all of functions | [funcs.py](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/funcs.py)
`usernames` | text (.txt) file | Stored database of users' emails | [usernames.txt](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/usernames.txt)
`passwords` | text (.txt) file | Stored database of users' hashed passwords | [passwords.txt](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/passwords.txt)
`birthdays` | text (.txt) file | Stored database of users' birthdays in MM/DD/YYYY format | [birthdays.txt](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/birthdays.txt)
