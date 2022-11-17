from states.default_state import DefaultState
from states.atm_states import ATMStates 

class ATMProcessor():
    def __init__(self):
        self.current_atm_state = ATMStates()

    @staticmethod
    def get_atm_object():
        atm_instance = ATMProcessor()
        atm_instance.set_current_atm_state(DefaultState())
        return atm_instance

    def set_current_atm_state(self, current_atm_state):
        self.current_atm_state = current_atm_state 

    
    def get_current_atm_state(self):
        return self.current_atm_state

    def print_current_atm_state(self):
        print(self.current_atm_state)

        
