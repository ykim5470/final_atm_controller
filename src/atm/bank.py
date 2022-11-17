import time
from atm.card import Card

class Bank():
    def __init__(self):
        self.name = None
        self.balance = 3000
        self.account = None
        self.card = None

    @staticmethod
    def get_card_object():
        atm_instance = Card()
        return atm_instance

    def set_current_card(self, current_atm_state):
        self.current_atm_state = current_atm_state 

    def get_current_card(self):
        return self.current_atm_state


    def create_account(self, card, account):
        # card from ATM machine
        print(card.get_holder_name())
        # account selection from ATM machine 
        print(account)

        self.card = card
        self.name = card.get_holder_name()
        self.account = account 
        return 
        
    def show_balance(self):
        holder = self.name 
        account = self.account 
        current_balance = self.balance
        print(f"{holder} at {account} left $ {current_balance}")
    
    def deposit(self, amount):
        # Check cash & read from cash bin
        self.delay()
        print(f"Your notes inserted is : {amount}")
        print("please enter 1 if the amount is correct")
        amount_confirm = input("")
        if amount_confirm == "1" :
            self.balance += amount 
            self.show_balance()
        else:
            print("Sorry! transaction terminated")
            print("Please take back cash and try again")
        return 

    def withdraw(self, amount):
        print(f"Your notes to withdraw are : {amount}")
        if self.balance > amount: 
            self.balance -= amount 
            self.show_balance()
        else:
            print("Over withdraw!")
            self.show_balance()

    

    
    @staticmethod
    def delay():
        time.sleep(3)
        