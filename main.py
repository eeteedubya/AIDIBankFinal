# date: Oct 2 2022
# author: E. Tyler Wilson
# student number: 100773241
# professor name: Marcos Bittencourt
# class and section: AIDI-1002-02
# filename: Main.py
# purpose:
#   Banking application that does simple banking functions.
#   Customer is created as an object that contains a list of Account objects
#   the account objects are actual accounts with types, account numbers, and
#   balances.


import Customer as cust
import Displays as d
import os
# constructor
if __name__ == '__main__':
# clear the screen
    os.system('cls')
# instantiate new customer as c
    c = cust.Customer()
# customer constructor asks for name. If customer enters "E"
# the program quits.  If a valid name is entered, the program goes
# to the main menu.
    if c.get_customer_name() == "E":
        print("Customer creation aborted. Exiting.")
        running = False
    else:
        d.display_main_menu(c)



