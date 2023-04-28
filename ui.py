


from bank import Bank as b
from os import system
from box_string import box_message as box, box_messages as box_list


class UI:

    @staticmethod
    def login_menu():
        """Menu for logging into an account; redirects to account_menu and create_account_menu."""

        while True:
            system('clear')
            print(f"""
{box("Welcome to the bank.")}
1) Log In
2) Create Account
3) Exit
""")
        
            i = input()
            if i == '1':
                account_num_input = ''
                pin_input = ''

                while True:
                    system('clear')
                    # Print account_num and pin
                    print(box_list([f"Account Number: {account_num_input}", f"PIN: {pin_input}"], 30))
                    
                    # account_num_input
                    if len(account_num_input) == 0:
                        print(box("Please enter your account number."))
                        temp_input = input()
                        if len(temp_input) > 0:
                            account_num_input = temp_input
                            continue

                    # pin_input
                    if len(pin_input) == 0:
                        print(box("Please enter your PIN."))
                        temp_input = input()
                        if len(temp_input) > 0:
                            pin_input = temp_input
                            continue
                    
                    # Attempt to log in
                    if b.test_login(account_num_input, pin_input):
                        UI.account_menu(account_num_input)
                    else:
                        system('clear')
                        print(box("Your account number or PIN is wrong. Press [Enter] to try again."))
                        input()


            elif i == '2':
                UI.create_account_menu()

            elif i == '3':
                b.end_database_connection()
                return
            



    @staticmethod
    def create_account_menu():
        pass


    @staticmethod
    def account_menu(account_num):
        pass


    @staticmethod
    def withdraw_menu(account_num):
        pass


    @staticmethod
    def deposit_menu(account_num):
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



╒════════════╕
│            │
╞════════════╡
│            │
│            │
│            │
╘════════════╛

╒════════════════════════════════╕
│ Account Number:                │
│ PIN:                           │
╞════════════════════════════════╡
│                                │
│                                │
╘════════════════════════════════╛

"""