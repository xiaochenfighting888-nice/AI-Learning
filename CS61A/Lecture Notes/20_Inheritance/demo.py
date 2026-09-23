class Account:
    interest = 0.02

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


class CheckingAccount(Account):
    """取款时收取手续费的账户"""

    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


class SavingsAccount(Account):
    """存款时收取手续费的储蓄账户"""

    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """
    同时具有支票账户和储蓄账户行为的账户

    >>> such_a_deal = AsSeenOnTVAccount("john")
    >>> such_a_deal.balance
    1
    >>> such_a_deal.deposit(20)
    19
    >>> such_a_deal.withdraw(5)
    13
    """

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1


class Bank:
    """管理多个账户并执行开户、付息等操作"""

    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        """创建账户、存入初始金额并加入银行账户列表"""
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        """为银行中的所有账户支付利息"""
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        """判断银行是否拥有超过一个账户"""
        return len(self.accounts) > 1
