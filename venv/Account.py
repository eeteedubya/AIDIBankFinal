# date: Oct 2 2022
# author: E. Tyler Wilson
# student number: 100773241
# professor name: Marcos Bittencourt
# class and section: AIDI-1002-02
# filename: Account.py
# purpose:
#   Simple account object.  contains randomly generated 12 digit account number,
#   an account type (chequing or savings) and a balance.
#   also contains a deposit and withdrawal wizard that gets validatad amounts
#

import random
import string
import math
from django.utils.crypto import get_random_string

class Account:
# constructor
    def __init__(self):
        #  account number
        _number: str
        #  account type
        _type: str
        # account balance
        _balance: float
        self._type = self.set_account_type()
        if self._type == "E":
            pass
        else:
            self._number = get_random_string(length=12, allowed_chars='0123456789')
            self._balance = 0.0

# getter returns _balance
    def get_balance(self):
        return self._balance
# getter returns _number
    def get_account_number():
        return _number

# sets account of (C)hequing, (S)avings, or (E)xit if user wants to abort
    def set_account_type(self):
        print("What type of account would you like to Open?\n")
        while True:
            type_selection = input("Please enter (C)hequing, (S)avings, or (E)xit:\n")
            if type_selection == "C" or type_selection == "c":
                return "Chequing"
            elif type_selection == "S"  or type_selection == "s":
                return "Savings"
            elif type_selection == "E"  or type_selection == "e":
                return "E"
            else:
                print("That is not a valid selection.\n")
# formatted return of number, type, and balance
    def to_string(self):
        return "{:15s} {:10s} ${:,.2f}\n".format(self._number, self._type, self._balance)

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

# gets an amount from user and validates if is a number, is positive, and not zero.
    def get_valid_amt(self, purpose):
        valid = False
        while valid == False:
            amt = input("Please enter the amount you wish to {}.\n".format(purpose))
            if self.isfloat(amt):
                if float(amt) > 0:
                    valid = True
                elif float(amt) == 0:
                    valid = False
                    print("You have requested to deposit $0.00. Nothing will be deposited.\n")
                else:
                    valid = False
                    print("Invalid entry. Please enter a positive amount without any symbols or letters.\n")
            else:
                valid = False
                print("Invalid entry. Please enter a positive amount without any symbols or letters.\n")
        return amt

# will get a valid amount and deposit using prompts.
    def deposit_wizard(self):
        self._balance += float(self.get_valid_amt("deposit"))

# will get a valid amount to withdraw using prompts and verifies there is
# enough in the account to cover the withdraw.
    def withdraw_wizard(self):
        amt = float(self.get_valid_amt("withdraw"))
        if amt <= self._balance:
            self._balance -= amt
        else:
            print("There are insufficient funds in this account to cover that withdrawal.\n")

# simple deposit without validation
    def deposit(self, amt):
        self._balance += float(amt)

# simple withdrawal without validation
    def withdraw(self, amt):
        if float(amt) <= self._balance:
            self._balance -= float(amt)
        else:
            print("There are insufficient funds in this account to cover that withdrawal.\n")

# displays balance in the form of a sentence
    def display_balance(self):
        print("\n")
        print("The balance of this account is: {}\n".format(self.get_balance()))



