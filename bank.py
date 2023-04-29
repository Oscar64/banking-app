


import sqlite3

# global variables for database access
connection = sqlite3.connect('bank_accounts.sqlite')
cursor = connection.cursor()

# initial setup - create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts 
(
    account_num INTEGER PRIMARY KEY,
    pin TEXT NOT NULL,
    user_name TEXT NOT NULL,
    current_balance REAL NOT NULL,
    address TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL
);
""")

class Bank:

    
    @staticmethod
    def create_new_account(pin, user_name, address, email, phone_number):
        """Creates & adds a new bank account to the database."""

        cursor.execute("""
        INSERT INTO accounts
        (
            pin,
            user_name,
            current_balance,
            address,
            email,
            phone_number
        ) 
        VALUES (?, ?, 0.0, ?, ?, ?);
        """, (pin, user_name, address, email, phone_number))
        # always call commit when updating table
        connection.commit()
        
        # to retreive the last inserted account number
        # MySQL has equivalent function: LAST_INSERT_ID()
        cursor.execute("SELECT last_insert_rowid();")
        last_id = cursor.fetchall()[0][0]
        
        return last_id


    @staticmethod
    def test_login(account_num, pin):
        """Returns true for false based on if the account number matches with the pin."""
    
        cursor.execute("""
            SELECT pin
            FROM accounts
            WHERE account_num = ?
            ;
            """, (account_num)
        )

        results = cursor.fetchall()
        if len(results) != 1 or results[0][0] != pin:
            return False
        return True


    @staticmethod
    def get_balance(account_num):
        """Returns the current_balance of an account."""

        cursor.execute("""
            SELECT current_balance
            FROM accounts
            WHERE account_num = ?
            ;
            """, (account_num)
        )

        results = cursor.fetchall()
        # if len(results) != 1:
        #     return None
        return results[0][0]


    # Returns True if amount is successfully withdrawn; returns False otherwise.
    @staticmethod
    def withdraw(account_num, amount):
        """Removes specified amount from current_balance of an account if that amount is available."""
    
        balance = Bank.get_balance(account_num)
        if balance - amount >= 0:
            cursor.execute("""
                UPDATE accounts
                SET current_balance = ?
                WHERE account_num = ?
                """, (round(balance-amount, 1), account_num)
            )
            connection.commit()
            return True
        
        return False


    @staticmethod
    def deposit(account_num, amount):
        """Adds specified amount to current_balance of an account."""

        balance = Bank.get_balance(account_num)
        cursor.execute("""
            UPDATE accounts
            SET current_balance = ?
            WHERE account_num = ?
            """, (balance+amount, account_num)
        )
        connection.commit()


    @staticmethod
    def get_info(account_num):
        """In a set order, returns the name, address, email, and phone_number of an account."""

        cursor.execute("""
            SELECT user_name, address, email, phone_number
            FROM accounts
            WHERE account_num = ?
            ;
            """, (account_num)
        )
        results = cursor.fetchall()[0]#[0]

        return results # [name, address, email, phone_number]


    @staticmethod
    def cancel_bank_account(account_num):
        """Removes a specified account from the database."""

        cursor.execute("""
            DELETE FROM accounts
            WHERE account_num = ?;
            """, (account_num)
        )
        connection.commit()


    @staticmethod
    def end_database_connection():
        """."""

        connection.close()
