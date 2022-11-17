import unittest

from atm.atm_processor import ATMProcessor


from states.default_state import DefaultState
from states.atm_states import ATMStates 

class TestAtmProcessor(unittest.TestCase):
    

    """
        atm Instnace 생성 
    """
    def test_atm_instance(self):
        self.atm = ATMProcessor.get_atm_object()     

        self.assertIsInstance(self.atm, ATMProcessor)


    """
        get_atm_object()로 Instance 생성 및 ATM 상태 설정을 Default로 업데이트
    """
    def test_atm_state_update(self):
        self.atm = ATMProcessor.get_atm_object()

        # get_atm_object() -> ATMStates to DefaultState update
        self.assertIsInstance(self.atm.current_atm_state, DefaultState)

    """
        ATM 시작하지 않았을 경우 ATM 상태는 ATMstates이다.
    """
    def test_atm_get_state(self):

        self.atm = ATMProcessor()
    
        self.assertIsInstance(self.atm.get_current_atm_state(), ATMStates)


    """
        ATM 시작 설정을 해줄 경우 ATM 상태 설정이 된다.
    """
    def test_atm_set_state(self):
        
        self.atm = ATMProcessor()
        self.assertIsInstance(self.atm.get_current_atm_state(), ATMStates)

        self.atm.set_current_atm_state(DefaultState())
        self.assertIsInstance(self.atm.get_current_atm_state(), DefaultState)
    