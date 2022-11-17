import random

from atm.atm import ATM

from states.atm_states import ATMStates
from states.idle_state import IdleState
from states.default_state import DefaultState
from states.error_state import ErrorState
from states.card_state import HasCardState




program = ATM()

program.initialize()

atm = program.atm
# ATM card reader inserted card
card = program.card

atm_balance = program.balance


# Pick any card from list
card_list = [
    {"_card_number" : "1234567891234", "_cvv" : "000", "_exp_date" : "12/23", "_card_type": "visa", "_holder_name": "lewis", "_pin_number" : "0000", "_bank_account": ["COMMONWEALTH", "NAB"]},
    {"_card_number" : "1234567891234", "_cvv" : "000", "_exp_date" : "12/23", "_card_type": "visa", "_holder_name": "alex", "_pin_number" : "0000", "_bank_account": ["WESTPAC", "NAB"]},
    {"_card_number" : "1234567891234", "_cvv" : "000", "_exp_date" : "12/23", "_card_type": "visa", "_holder_name": "dainel", "_pin_number" : "0000", "_bank_account": ["ANZ", "NAB"]},
    {"_card_number" : "1234567891234", "_cvv" : "000", "_exp_date" : "12/23", "_card_type": "visa", "_holder_name": "martin", "_pin_number" : "0000", "_bank_account": ["ANZ", "WESTPAC"]},
    ]


def switch(atm):
    state = type(atm.get_current_atm_state()).__name__
    if state == "DefaultState":
        print("Initial state")
        card_insert_action = int(input("Please insert card if you want to make a transaction : "))
        if card_insert_action == 1 :
            atm.set_current_atm_state(IdleState())
            return
    elif state == "IdleState":
        card_choice = random.choice(card_list)
        atm.get_current_atm_state().insert_card(atm, card_choice)
        return 
    elif state == "HasCardState":
        print("Your are now having card state")
        atm.get_current_atm_state().authenticate_pin(atm)
        return 
    elif state == "AccountSelectState":
        print("Please select one of the following accounts you have")
        atm.get_current_atm_state().show_accounts()
        account_select_action = int(input(""))
        atm.get_current_atm_state().select_account(atm, account_select_action)
        return
    elif state == "TransactionSelectState":
        print("Please select one of the following options")
        atm.get_current_atm_state().show_options()
        transaction_select_action = int(input(""))
        atm.get_current_atm_state().select_transaction(atm, atm_balance, transaction_select_action)
        return 
    else:
        atm.set_current_atm_state(ErrorState())
        atm.get_current_atm_state().exit(atm)


while True:
     switch(atm)



