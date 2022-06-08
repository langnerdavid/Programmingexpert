class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        print("run")
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid!")
        self._second = second


t = Time(54)
t.second = 59

class Time:
    def __init__(self, second):
        self._second = second

    def get_second(self):
        print("run")
        return self._second

    def set_second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid!")
        self._second = second

    second = property(get_second, set_second)


class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, balance):
        if balance < 0 and balance > 100000 and not balance.isdigit():
            return
        self._balance = balance