from states.default_state import DefaultState


class TransactionSelectState():
    def __init__(self, bank_card, target_bank_account):
        self.bank_card = bank_card
        self.target_bank_account = target_bank_account
        

    def show_options(self):
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")


    def select_transaction(self,atm, atm_balance, option):
        while True:
            if option == 1:
                self.target_bank_account.show_balance()
                return 
            if option == 2:
                print("Please insert cash in the bin ")
                amount = int(input(""))
                self.target_bank_account.deposit(amount)
                atm_balance += amount
                return
            if option == 3:
                print("Please enter withdrawal amount ")
                amount = int(input(""))
                if atm_balance < amount:
                    print("ATM has not enough balance! Sorry")
                    print("Try other transaction")
                self.target_bank_account.withdraw(amount)
                atm_balance -= amount
                return
            if option == 4:
                print("You entered exit")
                print("Please take your card :)")
                atm.set_current_atm_state(DefaultState())
                break


