# date: Oct 2 2022
# author: E. Tyler Wilson
# student number: 100773241
# professor name: Marcos Bittencourt
# class and section: AIDI-1002-02
# filename: Displays.py
# purpose:
#   Storage of display functions like menus.


import os

# collected methods to display all elements of the main
#  menu in one function
def display_main_menu(cust):
    running = True
    while running:
        text_welcome_banner()
        text_display_account_info(cust)
        running = text_display_options(cust)

# Standard welcome banner
def text_welcome_banner():
    os.system('cls')
    print("""
    *******************************************************************************
    
    WELCOME TO AIDI BANK!
    *******************************************************************************
    """)

# takes customer object and displays formatted name and account information from it.
def text_display_account_info(cust):
    print("""
Customer Name: {}
Accounts:
{:15s} {:10s} {:10s}
{}""".format(cust.get_customer_name(),"Acct#","Acct Type","Balance", cust.get_accounts_to_string()))

# main options menu
def text_display_options(customer):
    print("""
    Options:
    (1) Create Account:
    (2) Deposit Funds:
    (3) Withdraw Funds:
    (4) Transfer Funds:
    (5) Account Balance:
    (Q) Quit:
    """)
    # selection is the input/action choice from the user.
    #  it is typed as str because user can enter numbered selection
    #  or "q" to exit the program
    selction : str
    selection = input("Please make a choice:\n")
    match selection:
        case '1':
            # create account
            customer.create_new_account()
        case '2':
            # Deposit funds
            selected_acct = pick_an_account(customer)
            selected_acct.deposit_wizard()

        case '3':
            # Withdraw Funds
            selected_acct = pick_an_account(customer)
            selected_acct.withdraw_wizard()

        case '4':
            # Transfer Funds
            print("SELECT ACCOUNT TO TRANSFER FROM:\n")
            selected_acct_from = pick_an_account(customer)
            amt = float(selected_acct_from.get_valid_amt("transfer"))
            if amt <= float(selected_acct_from.get_balance()):
                selected_acct_from.withdraw(amt)
                print("SELECT ACCOUNT TO TRANSFER TO:\n")
                selected_acct_to = pick_an_account(customer)
                # take from the from account and deposit in the to account
                selected_acct_to.deposit(amt)
            else:
                print("insufficient funds in FROM account.")

        case '5':
            # Account Balance
            selected_acct = pick_an_account(customer)
            selected_acct.display_balance()

        case "Q"|"q":
            # Quit program
            print("You selected to QUIT:\n")
            return False
        case _:
            print("Selection not recognized.  Please Try Again:\n")
    return True

# for selecting an account.
# displays a numbered list of accounts owned by a customer.
# user selects the number of the account.
# Returns the account selected.
def pick_an_account(cust):
    running = True
# as we iterate over the accounts, the indexes are saved in this list
#  for further validation. the user selection is used as an index that
#  can be compared to this list.
    index_list = []
    while running == True:
        print("""{:15s} {:10s} {:10s}
        """.format("Acct#", "Acct Type", "Balance"))
# enumerating the accounts list so the indexes can be used as
#   numbered selections
        for indx, acct in enumerate(cust.get_accounts()):
            print("({}) {}".format(indx, acct.to_string()))
            index_list.append(indx)
# getting selected account
        acct_selection = input("Please select which account:\n")
# validating that the selected account exists.
        if acct_selection.isnumeric():
            if int(acct_selection) in index_list:
                running = False
            else:
                running = True
                print("Invalid selection. Please pick a number that matches an account.")
# returning the selected account
    return cust._accounts[int(acct_selection)]




