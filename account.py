class Account:
    """Creating a simple Account"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print('Account created for {0}.'.format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.showBalance()
    def withdrawal(self, amount):
        if amount > 0 and self.balance-amount > 0:
            self.balance -= amount
        else:
            print('Amount is not valid in reelation to your balance.')
        self.showBalance()
    
    def showBalance(self):
        print(f'Your Account balance is {self.balance}.')

if __name__ == '__main__':
    yash=Account('Yash', 0)
    yash.showBalance()
    
    yash.deposit(6000)
    yash.withdrawal(50000)
    # yash.showBalance()  