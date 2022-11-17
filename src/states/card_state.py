from states.account_select_state import AccountSelectState
from atm.card import Card

# Receive signal from card reader device with polling
class HasCardState():
    def __init__(self, bank_card):
        self.bank_card = bank_card
        self.bank_pin_number = self.bank_card.get_pin_number()
        self.bank_holder_name = self.bank_card.get_holder_name()
        print(self.bank_holder_name)


    def authenticate_pin(self, atm):
       if self.bank_pin_number ==  self.enter_pin_number():
        atm.set_current_atm_state(AccountSelectState(self.bank_card))
     
    @staticmethod
    def enter_pin_number():
        user_pin_number = input("Please Enter 4-digit PIN number : ")
        return user_pin_number
        