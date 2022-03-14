# Comprehensive User Management System

## Introduction

This code will allow the user to register an account that saves the email and password of the user. When logged in, the user can add/edit/view their birthday, delete their account and more. If the user forgets their password, this code will send a recovery email with a 6-digit recovery code to the user's email to reset their password.

## Functions

Function | Description
------------- | -------------
`main`  | Run main code which presents the user with a navigatable menu to begin their user management experience
`register`  | Generate the interactive menu of a page given an object
`get_dict_from_url`  | Return a dictionary based on the JSON response from SWAPI for a given URL
`

## Files

File | File Type | Description | Link
------------- | ------------- | ------------- | -------------
`main` | python (.py) file | Imports the functions file and then calls it | [main.py](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/main.py)
`funcs` | python (.py) file | Runs all of functions | [funcs.py](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/funcs.py)
`usernames` | text (.txt) file | Stored database of users emails | [usernames.txt](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/usernames.txt)
`passwords` | text (.txt) file | Stored database of users hashed passwords | [passwords.txt](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/passwords.txt)
`birthdays` | text (.txt) file | Stored database of users birthdays in MM/DD/YYYY format | [birthdays.txt](https://github.com/kehillah-coding-2022/user-management-EytanGF/blob/main/birthdays.txt)
