from decimal import Decimal
from datetime import datetime


class Manager:

    # @classmethod
    # def create(cls, **kwargs):
    #     print(cls)
    #     return cls(**kwargs)
    @classmethod
    def create(self, **kwargs):
        # print(self)
        print(kwargs['wallet'])
        return self(**kwargs)

    def delete(self):
        del self


class User(Manager):
    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class Wallet(Manager):
    __balance = Decimal(0)
    transactions = []

    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f"{self.user}: #{self.__balance}"  # Folu Ola: #0

    # def transactions(self):
    #     output = []
    #     for transaction in transactions:
    #         if transaction.wallet == self:
    #             output.append(transaction)
    #             # yield transaction
    #     return output

    def credit(self, amount: Decimal):
        balance_before = self.__balance
        self.__balance += amount
        print(self)
        transaction = Transaction.create(
            transaction_type="Credit", balance_before=balance_before, balance_after=self.__balance, wallet=self)
        self.transactions.append(transaction)

    def debit(self, amount: Decimal):
        balance_before = self.__balance
        self.__balance -= amount
        transaction = Transaction.create(
            transaction_type="Debit", balance_before=balance_before, balance_after=self.__balance, wallet=self)
        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)
            print(transaction.transaction_type)


class Transaction(Manager):
    def __init__(self, transaction_type, balance_before, balance_after, wallet):
        self.transaction_type = transaction_type
        self.balance_before = balance_before
        self.balance_after = balance_after
        self.wallet = wallet
        self.time = datetime.now()

    def __str__(self):
        return f"Transaction Type: {self.transaction_type}, Balance before: {self.balance_before}, Balance After: {self.balance_after}, Time: {self.time}"


user1 = User('Mayowa', 'Ola', 'mayowa@mail.com')
print(user1.email)
#
wallet = Wallet(user=user1)
# print(wallet.user)
# print(wallet.balance)
# print(wallet)
#
# user2 = User('Folu', 'Ola', 'folu@mail.com')
# # print(user2.email)
#
# wallet2 = Wallet(user=user2)
# print(wallet2.user)
# print(wallet2.balance)
# print(wallet2)

wallet.credit(Decimal(10))
wallet.debit(Decimal(50))
wallet.show_transactions()
