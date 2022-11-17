class Card():
    def __init__(self, number, cvv, exp_date, type, holder_name, pin_number, bank_account):
        self._number = number
        self._cvv = cvv
        self._exp_date = exp_date
        self._type = type
        self._holder_name = holder_name
        self._pin_number = pin_number
        self._bank_account = bank_account


    def get_pin_number(self):
        return self._pin_number


    def get_holder_name(self):
        return self._holder_name

        
    def get_accounts(self):
        return self._bank_account