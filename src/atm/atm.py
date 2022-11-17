from atm.atm_processor import ATMProcessor

class ATM():
    def __init__(self):
        self.atm = None 
        self.card = None
        self.balance = 20000

    def initialize(self):
        self.atm = ATMProcessor.get_atm_object()


        
        