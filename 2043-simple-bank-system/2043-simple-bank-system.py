class Bank:

    def __init__(self, balance: List[int]):
        self.i = 1
        self.balance = {}
        for M in balance:
            self.balance[self.i] = M
            self.i += 1
            
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < self.i and account2 <self.i:
            if money <= self.balance[account1]:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if account < self.i:
            self.balance[account] += money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account < self.i:
            # print(self.balance)
            if self.balance[account] >= money:
                self.balance[account] -= money
                return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)