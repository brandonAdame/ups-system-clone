# File: main.py


"""
This file will interact with the 'ups_db' 

Operation available:
    - Adding/removing a user
    - Adding/removing UPS store
    - Adding a package
"""

import sqlite3

def add_user():
    """
    This function will prompt the user to enter credentials for
    adding a user.

    Credentials needed: username, first name, last name, address, phone #

    This function assumes that duplicate accounts will never be created.
    """

    # Prompt user for credentials
    print("Hello! Please enter the following values:")
    print("username, first name, last name, address, phone #\n")

    # Save credentials in appropriate variables 
    username = input('username: ')
    first_name = input('first name: ')
    last_name = input('last name: ')
    address = input('address: ')
    phone = input('phone # [NO DASHES]: ')
    phone = int(phone)  # phone is originally str, convert to int

    print('{}, {}, {}, {}, {}'.format(username, first_name, last_name, address, phone))

    # Insert values into SQL db using SQL query
    print(type(phone))

    # Validate 'user' has been created


def open_db():
    """
    This function is used to test the connection to the DB
    is working correctly.

    It can also be modified later on.
    """
    db = sqlite3.connect('ups_db.db')

    cursor = db.cursor()
    cursor.execute('select * from ups_branch')
    print(cursor.fetchall())
    

    db.close()

if __name__ == "__main__":
    # open_db()
    add_user()