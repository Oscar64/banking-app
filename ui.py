


from os import system
from bank import Bank as b
from box_string import box_message as box, box_messages as box_list


class UI:

    @staticmethod
    def main_menu():
        """Menu for logging into an account; redirects to account_menu and create_account_menu."""

        while True:
            system('cls')
            print(f"""{box("Welcome to the bank.")}
1) Log In
2) Create Account
3) Exit
""")
        
            i = input()
            if i == '1':
                UI.login_menu()

            elif i == '2':
                UI.create_account_menu()

            elif i == '3':
                b.end_database_connection()
                system('cls')
                return
 

    @staticmethod
    def login_menu():
        """Menu for attempting to log into an account."""

        loop = True
        account_num_input = ''
        pin_input = ''

        while loop:
            system('cls')
            # Print account_num and pin
            print(box_list([f"Account Number: {account_num_input}", f"PIN: {pin_input}"]))

            # account_num_input
            if len(account_num_input) == 0:
                while True:
                    print(box('Please enter your account number. Enter "e" to leave.'))
                    temp_input = input()
                    if temp_input == 'e':
                        return

                    if len(temp_input) > 0 and len(temp_input) <= 10:
                        account_num_input = temp_input
                        break
                    system('cls')
                continue


            # pin_input
            if len(pin_input) == 0:
                while True:
                    print(box('Please enter your PIN. Enter "e" to leave.'))
                    temp_input = input()
                    if temp_input == 'e':
                        return

                    if len(temp_input) >= 4 and len(temp_input) <= 16:
                        pin_input = temp_input
                        break
                    system('cls')
                continue
            
            # Attempt to log in
            if b.test_login(account_num_input, pin_input):
                UI.account_menu(account_num_input)
                return
            else:
                system('cls')
                account_num_input = ''
                pin_input = ''
                print(box('Your account number or PIN is wrong. Press [Enter] to retry. Enter "e" to leave.'))
                i = input()
                if i == 'e':
                    break


    @staticmethod
    def create_account_menu():
        """Menu for creating a new account."""

        pin_input = ''
        user_name_input = ''
        address_input = ''
        email_input = ''
        phone_number_input = ''

        while True:
            system('cls')
            # Print account_num and pin
            print(box_list([f"PIN: {pin_input}",
                            f"Name: {user_name_input}",
                            f"Address: {address_input}",
                            f"Email: {email_input}",
                            f"Phone Number: {phone_number_input}",
                            ]))

            # pin_input
            if len(pin_input) == 0:
                t = UI.get_account_info_input('PIN', 4, 16)
                if t == 'left ♥ ♦ ♣ ♠':
                    return
                pin_input = t
                continue

            # user_name_input
            if len(user_name_input) == 0:
                t = UI.get_account_info_input('name', 3, 26)
                if t == 'left ♥ ♦ ♣ ♠':
                    return
                user_name_input = t
                continue

            # address_input
            if len(address_input) == 0:
                t = UI.get_account_info_input('address', 1, 37)
                if t == 'left ♥ ♦ ♣ ♠':
                    return
                address_input = t
                continue

            # email_input
            if len(email_input) == 0:
                t = UI.get_account_info_input('email', 3, 31)
                if t == 'left ♥ ♦ ♣ ♠':
                    return
                email_input = t
                continue

            # phone_number_input
            if len(phone_number_input) == 0:
                t = UI.get_account_info_input('phone number', 3, 17)
                if t == 'left ♥ ♦ ♣ ♠':
                    return
                phone_number_input = t
                continue

            # Create the account
            account_num = b.create_new_account(pin_input, user_name_input, address_input, email_input, phone_number_input)

            system('cls')
            print(box(f"New account successfully created. The account number is {account_num}; make sure to remember this! Type [Enter] to continue."))
            input()
            return
            

    # Requires information to be properly storable as a String.
    # Will repeatedly prompt the user until an input of a valid length is given.
    @staticmethod
    def get_account_info_input(name, min_length, max_length):
        """Prompts the user for a certain type of information."""
        while True:
            print(box(f'Please enter your {name} (Required length of {min_length}-{max_length}). Enter "e" to leave.'))
            temp_input = input()
            if temp_input == 'e':
                return 'left ♥ ♦ ♣ ♠'

            if len(temp_input) >= min_length and len(temp_input) <= max_length:
                return temp_input
            system('cls')



    @staticmethod
    def account_menu(account_num):
        """Primary menu for a bank accout; shows all basic/necessary information."""

        while True:
            [name, address, email, phone_number] = b.get_info(account_num)
            balance = b.get_balance(account_num)
            system('cls')
            print(box_list([f"Current Balance: ${balance}",
                            " ",
                            f"Name: {name}",
                            f"Address: {address}",
                            f"Email: {email}",
                            f"Phone Number: {phone_number}"
                            ]))
            print(box_list(["1) Withdraw",
                            "2) Deposit ",
                            "3) Cancel Account ",
                            "4) Log Out"
                            ]))

            i = input()
            if i == '1':
                UI.withdraw_menu(account_num)

            elif i == '2':
                UI.deposit_menu(account_num)

            elif i == '3':
                if UI.cancel_account_menu(account_num):
                    return

            elif i == '4':
                return


    @staticmethod
    def withdraw_menu(account_num):
        """Prompts user for them to withdraw money from their account."""

        balance = b.get_balance(account_num)
        while True:
            system('cls')
            print(box(f"Current Balance: {balance}"))
            print(box('How much money would you like to withdraw? Enter "e" to leave.'))

            w_input = input()
            if w_input == 'e':
                return
            if len(w_input) > 0:
                try:
                    amount = round(float(w_input.replace('$', '', 1)), 2)
                    if b.withdraw(account_num, amount):
                        system('cls')
                        print(box(f'${amount} has successfully been withdrawn. Press [Enter] to continue.'))
                        input()
                        return
                    else: # not enough money
                        system('cls')
                        print(box(f'The balance is too low to withdraw ${amount}. Press [Enter] to retry.'))
                        input()
                        return
                except TypeError:
                    system('cls')
                    print(box('That is not a valid amount. Press [Enter] to retry.'))
                    input()


    @staticmethod
    def deposit_menu(account_num):
        """Prompts user for them to deposit money into their account."""

        balance = b.get_balance(account_num)
        while True:
            system('cls')
            print(box(f"Current Balance: {balance}"))
            print(box('How much money would you like to deposit? Enter "e" to leave.'))

            d_input = input()
            if d_input == 'e':
                return
            if len(d_input) > 0:
                try:
                    amount = round(float(d_input.replace('$', '', 1)), 2)
                    b.deposit(account_num, amount)
                    system('cls')
                    print(box(f'${amount} has successfully been deposited. Press [Enter] to continue.'))
                    input()
                    return
                except TypeError:
                    system('cls')
                    print(box('That is not a valid amount. Press [Enter] to retry.'))
                    input()


    # Returns true if the account is deleted, false otherwise.
    @staticmethod
    def cancel_account_menu(account_num):
        """Prompts user for their PIN and confirmation for deleting their account."""
        pin = '_'

        while True:
            system('cls')
            print(box('For confirmation, please enter the PIN of this account. Enter "e" to leave.'))

            p = input()
            if p == 'e':
                return False
            if len(p) >= 4 and len(p) <= 16:
                pin = p
            else:
                system('cls')
                print(box('An invalid PIN was entered. Press [Enter] to retry.'))
                input()
                continue

            # Test account PIN
            if b.test_login(account_num, pin):
                system('cls')
                print(box('The correct PIN has been entered. Are you sure you would like to cancel this account? Type "Yes." to confirm, [Enter] to leave.'))

                c = input()
                if c == 'Yes.':
                    b.cancel_bank_account(account_num)
                    system('cls')
                    print(box(f'Account number {account_num} has successfuly been closed. Press [Enter] to continue.'))
                    input()
                    return True

            else: # incorrect pin
                system('cls')
                print(box('The entered PIN is incorrect. Press [Enter] to retry.'))
                input()


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