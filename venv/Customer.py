# date: Oct 2 2022
# author: E. Tyler Wilson
# student number: 100773241
# professor name: Marcos Bittencourt
# class and section: AIDI-1002-02
# filename: Customers.py
# purpose:
#   Simple Customer object.  Contains a private list of accounts called _accounts
#   and a _name.
#

import re
import Account as a

class Customer:
# list of accounts. as accounts are created, they are added to this list as an
# accounts object.
    _accounts = []

# constructor
    def __init__(self):
        _name: str
        self._name = self.set_customer_name()
# getter of _name
    def get_customer_name(self):
        return self._name
# getter of _accounts
    def get_accounts(self):
        return self._accounts

# dialogue for customer to enter name. Will loop until customer
#   confirms name entered is correct.
    def set_customer_name(self):
        while True:
            input_name = input("Please enter your name:\n")
            print("You entered {}.".format(input_name))
            confirm_name = input("Is this correct? (y/n) or (E)xit:")
            if confirm_name == "Y" or confirm_name == "y":
                break
            elif confirm_name == "N" or confirm_name == "n":
                input_name = ""
                continue
# user can exit the program if they select E to exit
            elif confirm_name == "E" or confirm_name == "e":
                input_name = "E"
                break
            else:
                print("Invalid selection.\n")
        return input_name

# creates a new account object and adds it to the _accounts list
    def create_new_account(self):
        n_acct = a.Account()
        self._accounts.append(n_acct)

# returns a string of account numbers, account types, and balances
#  in columns
    def get_accounts_to_string(self):
        acct_string = ""
        for acct in self._accounts:
            acct_string += acct.to_string()
        return acct_string

