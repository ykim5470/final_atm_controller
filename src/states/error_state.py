from states.default_state import DefaultState

class ErrorState():
    def __init__(self):
        print("Error occured")

    def exit(self, atm):
        atm.set_current_atm_state(DefaultState())
        print("ByeBye")
        quit()

        
