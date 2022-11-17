from states.transaction_select_state import TransactionSelectState
from atm.bank import Bank

class AccountSelectState():
    def __init__(self, bank_card):
        self.bank_card = bank_card
        self.bank_holder_name = self.bank_card.get_holder_name()
        self.bank_account = self.bank_card.get_accounts()


    def show_accounts(self):
        count = 0
        for i in self.bank_account:
            count += 1
            print(f"{count} : {i}")
        
        

    def select_account(self, atm, selected_account):
        if selected_account in range(1, len(self.bank_account)+1):
            selected_account = self.bank_account[selected_account-1]
            # Assume account information has been created already, but here just create a bank account here
            target_bank_account = Bank()
            target_bank_account.create_account(self.bank_card, selected_account)
            atm.set_current_atm_state(TransactionSelectState(self.bank_card, target_bank_account))
        else:
            print("Invliad option")
        