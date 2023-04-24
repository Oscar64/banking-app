






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
┌┬─┐
││ │
├┼─┤
└┴ ┘


╢╖╕╣║╗╝╜╛╟╚╔╩╦╠╬╧╨╤╥╙╘╒╓╫╪


╞═╡




"""