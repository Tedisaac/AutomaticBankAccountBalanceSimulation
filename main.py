class AutoBank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(self.name + " : ")
            print(self.balance)

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print(self.name + " : ")
            print(self.balance)
        else:
            print("Insufficient funds")

    def transfer(self, amount, account):
        if 0 < amount < self.balance:
            self.balance = self.balance - amount
            account.balance = account.balance + amount
            print(self.name + " : ")
            print(self.balance)
            print(account.name + " : ")
            print(account.balance)
        else:
            print(self.name + " : ")
            print("Insufficient funds")

    def balances(self):
        print(self.name + "'s balance is : ")
        print(self.balance)


wanjiru = AutoBank("Wanjiru", 0)
linda = AutoBank("Linda", 0)
juma = AutoBank("Juma", 0)
wanjiru.deposit(152.00)
wanjiru.transfer(218.25, linda)
linda.deposit(154.00)
wanjiru.transfer(97.50, juma)
linda.deposit(156.00)
wanjiru.transfer(246.75, linda)
juma.deposit(1557.17)
linda.withdraw(20.00)
wanjiru.deposit(158.00)
wanjiru.withdraw(159.00)
linda.deposit(160.00)
linda.deposit(162.00)
juma.transfer(2000.00, linda)
wanjiru.deposit(164.00)
wanjiru.withdraw(165.00)
juma.deposit(1757.92)
wanjiru.withdraw(166.00)
linda.withdraw(167.00)
linda.deposit(169.00)
wanjiru.transfer(300.00, juma)
wanjiru.deposit(171.00)
linda.deposit(174.00)
linda.transfer(2000.00, juma)
juma.deposit(1757.92)
wanjiru.withdraw(175.00)
linda.withdraw(176.00)
wanjiru.deposit(178.00)
wanjiru.transfer(500.00, linda)
linda.deposit(180.00)
wanjiru.withdraw(181.00)
wanjiru.deposit(182.00)
juma.transfer(500.00, linda)
wanjiru.deposit(184.00)
wanjiru.transfer(600.00, juma)
wanjiru.deposit(188.00)
wanjiru.balances()
linda.balances()
juma.balances()
