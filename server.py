class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        print(f"You have deposited: ${amount}")
        self.balance += amount
        return self

    def withdraw(self, amount):
        print(f"You Withdrew: ${amount}")
        if (self.balance < amount):
            print("Insufficient Funds... Charging a $5 fee")
            self.balance -+ 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Your Balance is: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


account1 = BankAccount(0.05, 1000)
account2 = BankAccount(0.05, 1500)

print("Account1 Info")
print("-------------")
account1.display_account_info().deposit(100).deposit(20).deposit(5).withdraw(150).yield_interest().display_account_info()
print("************************************************")
print("Account2 Info")
print("-------------")
account2.display_account_info().deposit(2000).deposit(55).withdraw(50).withdraw(135).withdraw(450).withdraw(80).yield_interest().display_account_info()

