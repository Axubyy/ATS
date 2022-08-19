import csv
from operator import ge
import random
import string


class Wallet:
    random_digits = string.digits
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase

    def __init__(self, wallet_balance=1000) -> None:
        self.wallet_balance = wallet_balance
        random_digits = string.digits
        upper_letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        generate_wallet_address = "".join(random.sample(random_digits, 4)) + "".join(
            random.sample(upper_letters, 3)) + "".join(random.sample(lower_letters, 3))
        self.wallet_address = generate_wallet_address

    @property
    def get_wallet_address(self):
        return self.wallet_address


class Transaction:
    def __init__(self) -> None:
        self.address = Wallet.get_wallet_id()
        self._balance = User.get_user_balance()

    def deposit_to_self(self, amount, wallet_address):
        users_data = User.get_csv_data()
        for user in users_data:
            if user["wallet_address"] == wallet_address:
                user['wallet_balance'] += amount
                self._balance += amount

    def deposit_to_others(self, amount, user_account_num, target_account_num):
        # Implicitly testing for valid account number
        if self.get_balance() > self._balance:
            self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def transfer(self, from_wallet_id, to_wallet_id, amount_out):
        self.withdraw(amount_out)
        self.deposit(amount_out)

    def log_transaction(self):
        pass

    def log_transaction(self, user_id, username):
        users_logs = self.get_transaction_data()
        for user_log in users_logs:
            if user_log["username"] == username & user_log["user_id"] == user_id:

                return

    @staticmethod
    def get_transaction_data():
        with open('csv_user_transactions.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)


class User:

    random_digits = string.digits
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    user_pin = random.sample(random_digits, 5)

    user_header = ["firstname", "lastname", "username",
                   "phone_number", "wallet_ID", "pin", "balance"]
    wallet_header = ["wallet_ID", "amount", "balance"]

    def __init__(self) -> None:
        self.account_balance = Wallet().balance
        self.wallet_address = Wallet().wallet_address

    def create_user(self, firstname, lastname, username, password):
        wallet_address = self.account_balance.get_wallet_id()

        user_data = {
            "firstname": firstname,
            "lastname": lastname,
            "username": username,
            "password": password,
            "wallet_adress": wallet_address,
            "balance": self.account_balance
        }

        self.save_data(user_data)

        return

    @staticmethod
    def save_data(data):
        with open('csv_user_data.csv', "w+") as ft:
            ft.write(data)

    @staticmethod
    def get_csv_data():
        with open('csv_user_data.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)

    def delete_user(self, username, firstname):
        users_data = self.get_csv_data()
        for user in users_data:
            if user["username"] == username & user["firstname"] == firstname:
                del user

    @property
    def get_user_wallet_balance(self):
        return self.wallet_balance

    @property
    def get_user_wallet_address(self):
        return self.wallet_address


u1 = User('John Doe', '19371554951', 20000)
u2 = User('Jenny Doe',  '19371564761', 20000)
print(u1.balance)
print(u2.balance)
User.transfer(u1, u2, 10)
print(u1.balance)
print(u2.balance)
