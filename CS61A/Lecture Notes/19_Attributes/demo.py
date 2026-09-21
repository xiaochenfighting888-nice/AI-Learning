class Account:
    interest = 0

    def __init__(self, account_holder):
        """初始化账户，设置账户持有人和初始余额"""
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """存入指定金额，并返回存款后的余额"""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """取出指定金额，如果余额不足则提示失败"""
        if self.balance < amount:
            return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance


if __name__ == "__main__":
    tom = Account("Tom")

    print(tom.deposit(100))
    print(tom.withdraw(30))
    print(tom.balance)
    tom.interest = 0.08

    print(tom.interest)
    print(Account.interest)
