# creating class for account and creating methods

class Account:
    """Creating a simple Account"""

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        print('Account created for {0}.'.format(self.name))
        self.showBalance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.showBalance()
    def withdrawal(self, amount):
        if amount > 0 and self.__balance-amount > 0:
            self.__balance -= amount
        else:
            print('Amount is not valid in relation to your balance.')
        self.showBalance()
    
    def showBalance(self):
        print(f'Your Account balance is {self.__balance}.')

if __name__ == '__main__':
    yash=Account('Yash', 50)
    # yash.showBalance()
    
    yash.deposit(6000)
    yash.withdrawal(5000)
    # yash.showBalance()    

    yug=Account('Yug',0)
    yug.__balance=200
    yug.deposit(300)
    yug.withdrawal(100)
