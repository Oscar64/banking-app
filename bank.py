import sqlite3

# global variables for database access
connection = sqlite3.connect('bank_accounts.sqlite')
cursor = connection.cursor()

# initial setup - create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts 
(
    account_num INTEGER PRIMARY KEY,
    pin INTEGER,
    user_name TEXT,
    current_balance REAL,
    address TEXT,
    email TEXT,
    phone_number TEXT,
);
""")

def create_new_account(pin, user_name, current_balance, address, email, phone_number):

  cursor.execute("""
    INSERT INTO accounts (
        pin, user_name, address, current_balance
        ) 
    VALUES (?, ?, ?, 0.0);
    """, (pin, address, user_name))
    # always call commit when updating table
    connection.commit()
    
    # to retreive the last inserted account number
    # MySQL has equivalent function: LAST_INSERT_ID()
    cursor.execute("SELECT last_insert_rowid();")
    last_id = cursor.fetchall()[0][0]
    
    return last_id

def get_balance(account_num):

    cursor.execute("""
        SELECT current_balance
        FROM accounts
        WHERE account_num = ? AND pin = ?
        ;
        """, (account_num, pin)
    )

    results = cursor.fetchall()
    if len(results) != 1:
        return None
    return results[0][0]

# def withdraw(account_num):

# def deposit(account_num):

#     can update address, email, and phone number
# def update_account_info(account_num):

# def cancel_bank_account(acccount_num):



# to add deposit or withdrawal functionality
# read about UPDATE statement in SQL


class Bank:

    @staticmethod
