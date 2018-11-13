import sqlite3
import getpass

## Make a connection to the database
conn = sqlite3.connect("")
cursor = conn.cursor()
# Next statement is for testing if the connection works. Uncomment it and change the table name.
# cursor.execute("SELECT * FROM Table")



## Have user log in
# Variable to flag whether or not the user has been authenticated
authenticated = False

while authenticated == False:
    # Get Credentials
    print("Enter your username")
    username = input()
    print("Enter your password")
    password = getpass.getpass()
    
    ## Check if user credentials exists and is correct
    authSQL = "SELECT * FROM Table WHERE Username = ? AND Password = ?",  username, password
    print(authSQL)
    #cursor.execute("SELECT * FROM Table WHERE Username = ? AND Password = ?",  username, password)
    if username == "a" and password == "a":
        print("Login Successful")
        authenticated = True
    else:
        # If not correct, prompt user that the info is incorrect and to retry
        print("Incorrect credentials. Please try again.")



## Once the user logs in, do one or two things:
#   1. Prompt them to enter the package info to see the status of it
#   2. Automatically show them the status of all their packages.



## If option 1, prompt them to either exit or reenter another package info
## If option 2, automatically close



## Option 1 will be useful for users that have a lot of packages
## Option 2 will be a quicker implementation



## Can have an option for only displaying packages based on their status.
# [1] Processing, [2] In Transit, [3] Delivered


## For keeping the terminal open
input()