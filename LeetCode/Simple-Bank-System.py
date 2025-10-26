# LeetCode
# 2043, Simple Bank System / Easy

class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)

    def _valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        if not self._valid(account1) or not self._valid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        if not self._valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        if not self._valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
