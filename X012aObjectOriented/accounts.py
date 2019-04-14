import pytz
import datetime


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for {}.".format(self._name))
        self.showbalance()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.showbalance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdrawl(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("your balance is {}, which is not sufficient.".format(self._balance))
        self.showbalance()

    def showbalance(self):
        print("Balance is :{}".format(self._balance))

    def account_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


tim = Account("Tim", 0)
# tim.showbalance()

tim.deposit(2000)
# tim.showbalance()

tim.withdrawl(1000)
# tim.showbalance()

tim.account_transaction()

steph = Account("Steph", 2000)
steph._balance = 200  # s0 its doesnt show s a warning as this is private  starting with _ but upto developer to remem
steph.deposit(200)
steph.withdrawl(100)
steph.account_transaction()
