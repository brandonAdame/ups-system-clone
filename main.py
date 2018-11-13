# File: main.py
# Last Updated: 11/10/18

"""
This file will interact with the 'ups_db' 

Operation available:
    - Adding/removing a user
    - Adding/removing UPS store
    - Adding a package
"""

import sqlite3

def open_db():
    db = sqlite3.connect('ups_db.db')

    # cursor = db.cursor()
    

    db.close()

if __name__ == "__main__":
    open_db()