# import csv
from decimal import Decimal
from inspect import trace
import random
import string


# class Wallet:
#     def __init__(self)  -> None:
#             random_digits = string.digits
#             upper_letters = string.ascii_uppercase
#             generate_wallet_address =  "".join(random.sample(random_digits,4)) + "".join(random.sample(upper_letters,3))
#             self.wallet_address = generate_wallet_address


#     def get_wallet_address(self):
#         return self.wallet_address
#         _

# class  Transactions:
#     def __init__(self) -> None:
#         self.transaction_log = []


#     def log_transaction(self):
#         for transaction_log in self.transaction_log:
#             print(str(transaction_log))
#         return


# class User(Wallet,Transactions):

#     random_digits = string.digits
#     pin_code  = "".join(random.sample(random_digits,5))

#     def __init__(self,firstname,lastname,username) -> None:
#         super().__init__()
#         self.firstname = self._is_valid_names(firstname)
#         self.lastname = self._is_valid_names(lastname)
#         self.username = self._is_valid_names(username)
#         self.pin_code = User.pin_code
#         self.wallet_address = Wallet().get_wallet_address(),
#         self.balance = 0
#         self.user_data_list = []

#     @property
#     def _is_valid_names(self, name_value):
#         if len(name_value) > 20:
#             raise ValueError("Cannot exceed 20 characters.")
#         return name_value

#     def save_user(self):


#         user_data = {
#             "firstname":self.firstname,
#             "lastname":self.lastname,
#             "username":self.username,
#             "pin_code": self.pin_code,
#             "wallet_address": self.wallet_address,
#             "balance":self.balance
#         }
#         self.user_data_list.append(user_data)
#         print(f"Your private pin code is {self.pin_code} and wallet address {self.wallet_address}")
#         print(self.user_data_list)
#         return "User Saved Successfully"

#     def delete_user(self,user_firstname,pin_code):
#         user_data = self.user_data_list
#         user = input("kindly input your username")
#         pin = input("kindly input your pin")
#         for data in user_data:
#             if data["firstname"] == user_firstname and data['pin_code'] == pin_code:
#                 print("You will be missed, GOODBYE!!")
#                 del data
#                 return "Deletion Successful"
#             else:
#                 print("Invalid Firstname or Pin code!!")
#                 return

#     def deposit_to_self(self, amount,wallet_address,pin_code):
#         user_data = self.user_data_list
#         for d in user_data:
#             try:
#                 if d["wallet_address"] == wallet_address and d["pin_code"] == pin_code:
#                     d["balance"] += amount
#                     d["deposits"] = 1 if not d["deposits"]  else +1
#                     Transactions.transaction_log.append(f"Account owner made a deposit of {amount} to their address{wallet_address}")
#                     print(f"You have Successfully deposited {amount} to your account")
#             except:
#                     print("Oops!", "Error occurred.")
#                     print("Next entry.")
#                     print()
#             return "yes"


#     def debit_wallet(self,wallet_address,amount):
#         user_data = self.user_data_list
#         for user in user_data:
#             if user["wallet_address"] == wallet_address:
#                 user["balance"] -= amount
#                 user["debits"] += 1 if user["debits"]  else 1
#                 Transactions.transaction_log.append(f"A deduction of {amount} to the address{wallet_address}")
#                 print(f"You have been debited the sum of {amount} to your account")
#                 return


#     def credit_wallet(self,wallet_address,amount):
#         user_data = self.user_data_list
#         for user in user_data:
#            if user["wallet_address"] == wallet_address:
#                user["balance"] -= amount
#                user["debits"] += 1 if user["debits"] else 1
#                Transactions.transaction_log.append(
#                    f"You have been credited with {amount} in your address{wallet_address}")
#                print(
#                    f"You have been credited the sum of {amount} to your account")
#                return


class Manager:
    @classmethod
    def create(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @classmethod
    def delete(cls):
        del cls


class User(Manager):
    def __init__(self, first_name):
        self.first_name = first_name

    def __str__(self) -> str:
        return self.first_name


class Transaction(Manager):
    def __init__(self, transaction_type, amount, wallet_address, old_balance, new_balance, depositor: str) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.wallet_address = None
        self.depositor = ''

        def __str__(self):
            return "Welcome" + self.new_balance + self.wallet_address + self.amount


class Wallet(Manager):
    random_digits = string.digits
    upper_letters = string.ascii_uppercase
    generate = str(''.join(random.sample(upper_letters, 3)) +
                   ''.join(random.sample(random_digits, 4)))
    print(generate)
    wallet_address = generate
    transactions = []
    balance = Decimal(0)

    def __init__(self, user) -> None:
        self.user = user

    def credit(self, amount):
        old_balance = self.balance
        self.balance = old_balance + amount
        transaction = Transaction.create(
            transaction_type="Credit", amount=40000, old_balance=old_balance, new_balance=self.balance, wallet_address=self.wallet_address, depositor='Megan')
        self.transactions.append(transaction)

    def debit(self, amount):
        old_balance = self.balance
        self.balance -= amount
        transaction = Transaction.create(amount=amount, transaction_type="Debit", old_balance=old_balance, new_balance=self.balance, wallet_address=self.wallet_address,
                                         depositor='Megannnn')
        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            print("Transact:", transaction.amount,
                  transaction.transaction_type)

    def __str__(self) -> str:
        return self.user + self.balance


u1 = User("Good-luck")
# print(u1)
# # u2 = User('Jenny Doe',  '19371564761', 20000)
# value = 7513ZSW
# print(u1.save_user())
# print(u1.deposit_to_self(3000, "7438XAB", "7492"))
# print(u1.log_transaction())
# # print(u2.balance)
# User.transfer(u1, u2, 10)
w1 = Wallet(u1)
w1.credit(35)
print(w1.debit(10))
w1.show_transactions()
