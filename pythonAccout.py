class Account:

    def __init__(self, balance, account_name):
        self.balance = balance
        self.account_name = account_name

    def __str__(self):
        return self.balance + ' ' + self.account_name

    def withdrawl(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return 'WithDrawl Successful for amount {0}'.format(amount)
        else:
            return 'WithDrawl unsuccessful'

    def deposit(self, amount):
        self.balance += amount;
        return 'deposit successful for the amount {0}'.format(amount)


account = Account(500, 'Saving Account')
print(account.withdrawl(300))
