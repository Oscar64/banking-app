


import unittest
from bank import Bank as b

class TestBank(unittest.TestCase):

    account_num = str(b.create_new_account('00000', 'user_name', 'address', 'email', 'phone_number'))

    def test_test_login(self):
        self.assertTrue(b.test_login(TestBank.account_num, '00000')) # Correct account_num and pin
        self.assertFalse(b.test_login('0', '111111')) # Incorrect account_num and pin

    def test_balance_methods(self):
        """Tests get_balance(), deposit(), and withdraw()."""
        
        b.deposit(TestBank.account_num, 1000)
        # Tests initial deposit & get_balance()
        self.assertEqual(b.get_balance(TestBank.account_num), 1000)
        # Tests different withdrawals
        self.assertFalse(b.withdraw(TestBank.account_num, 1050)) # Tries to withdraw too much
        self.assertTrue(b.withdraw(TestBank.account_num, 500))

        self.assertEqual(b.get_balance(TestBank.account_num), 500)
        





unittest.main()

b.cancel_bank_account(TestBank.account_num)
b.end_database_connection()
