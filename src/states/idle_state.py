import time
from states.card_state import HasCardState

from atm.card import Card 


class IdleState():     
    def __init__(self):
        print("Wait please")
           

    def insert_card(self, atm, card):
        # Card Read process will be integrated later
        self.delay()
        
        # card data store in RAM & request to bank system
        bank_card = Card(card["_card_number"], card["_cvv"], card["_exp_date"], card["_card_type"],card["_holder_name"], card["_pin_number"], card["_bank_account"])

        atm.set_current_atm_state(HasCardState(bank_card))

    @staticmethod
    def delay():
        time.sleep(3)
