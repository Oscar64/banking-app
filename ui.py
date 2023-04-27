


from bank import Bank as b
from os import system
import getkeys


class UI:

    @staticmethod
    def login_menu():
        while True:
            system('clear')
            print("""
1) Log In
2) Create Account
3) Exit
""")
            
            



    @staticmethod
    def create_account_menu():
        pass


    @staticmethod
    def account_menu():
        pass


    @staticmethod
    def withdraw_menu():
        pass


    @staticmethod
    def deposit_menu():
        pass


"""
# sample interaction with banking app:
new_id = create_new_account('misha', 12345)
print('created account number:', new_id)
print('remember this number to access it in the future')
print()

# balance check with correct pin
balance = check_balance(new_id, 12345)
print(f'(correct pin) balance for account #{new_id} is {balance}')

# balance cehck with incorrect pin
balance = check_balance(new_id, 5678)
print(f'(wrong pin) balance for account #{new_id} is {balance}')

"""

"""
┌┬─┐ ╔╦═╗ ╒╤═╕ ╓╥─╖
││ │ ║║ ║ ││ │ ║║ ║
├┼─┤ ╠╬═╣ ╞╪═╡ ╟╫─╢
└┴─┘ ╚╩═╝ ╘╧═╛ ╙╨─╜
"""