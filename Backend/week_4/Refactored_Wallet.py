import csv
import random
import string
import pandas as pd


class Wallet:
    random_digits = string.digits
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    generate_wallet_address = "".join(random.sample(
        random_digits, 4)) + "".join(random.sample(upper_letters, 3))
    wallet_header = ["wallet_addresses", "amounts",
                     "balances", "deposits", "debits"]

    def __init__(self) -> None:
        random_digits = string.digits
        upper_letters = string.ascii_uppercase
        generate_wallet_address = "".join(random.sample(
            random_digits, 4)) + "".join(random.sample(upper_letters, 3))
        self.wallet_address = generate_wallet_address
        pass

    @property
    def get_wallet_address(self):
        return self.wallet_address
        _

    def deposit_to_self(self, amount, wallet_address, pin_code=None):
        users_data = User.get_csv_data()
        for u, d in users_data:
            if d["wallet_addresses"] == wallet_address and d["pin_code"] == pin_code:
                Wallet.save_wallet_data(amounts=amount, wallet_addresses=wallet_address, balances=int(
                    d["balances"])+amount, deposits=1, debits=None)

                self._balance += amount

    def debit_wallet(wallet_address, amount):
        user_data = User.get_csv_data()
        for u, d in user_data:
            if d["wallet_addresses"] == wallet_address:
                Wallet.save_wallet_data(amounts=amount, wallet_addresses=wallet_address, balances=int(
                    d["balances"])+amount, deposits=None, debits=1)

    def credit_wallet(wallet_address, amount):
        user_data = User.get_csv_data()
        for u, d in user_data:
            if d["wallet_addresses"] == wallet_address:
                Wallet.save_wallet_data(amounts=amount, wallet_addresses=wallet_address, balances=int(
                    d["balances"])+amount, deposits=1, debits=None)
        pass

    def transfer(self, from_wallet_address, to_wallet_address, amount_out):
        user_data = User.get_csv_data()
        for k, v in user_data:
            if v["wallet_addresses"] == from_wallet_address and v["balance"] > amount_out:
                Wallet.debit_wallet(from_wallet_address, amount_out)
            if v["wallet_address"] == to_wallet_address:
                Wallet.credit_wallet(to_wallet_address, amount_out)

    @staticmethod
    def save_wallet_data(**args):
        with open("wallet_data.csv", "w", newline="\n") as wallet_file:
            writer = csv.DictWriter(
                wallet_file, fieldnames=Wallet.wallet_header)
            writer.writeheader()
            writer.writerow(**args)
        return "Registration Successful"


class Transaction:
    def __init__(self) -> None:
        self.address = Wallet.get_wallet_id()
        self._balance = User.get_user_balance()

    @staticmethod
    def log_transaction(self):
        df = pd.read_csv("wallet_data.csv")
        df.head()
        pd.options.display.max_columns = len(df.columns)

    @staticmethod
    def get_wallet_data():
        with open('wallet_data.csv', 'r') as wallet_file_text:
            data = csv.DictReader(wallet_file_text)
            return list(data)


class User(Wallet):

    random_digits = string.digits
    pin_code = "".join(random.sample(random_digits, 5))

    user_header = ["firstname", "lastname", "username",
                   "pin_code", "wallet_address", "balance"]

    def __init__(self) -> None:
        super().__init__()

        # self.account_balance = Wallet().wallet_balance
        # self.wallet_address = Wallet().wallet_address
        # self.wallet = Wallet()

    def create_user(self, firstname, lastname, username):
        # implement as inputs

        user_data = {
            "firstname": firstname,
            "lastname": lastname,
            "username": username,
            "pin_code": User.pin_code,
            "wallet_address": Wallet.get_wallet_address(),
            "balance": 0
        }

        print(
            f"Here are ,your ID, and your pin is {User.pin_code}, Dont disclose this!")

        with open("user_data.csv", "a", newline="\n") as user_file:
            writer = csv.DictWriter(user_file, fieldnames=User.user_header)
            # writer.writeheader()
            writer.writerow(user_data)
        return "Registration Successful"

    def delete_user(self):
        data = User.get_csv_data()
        user = input("kindly input your username")
        pin = input("kindly input your pin")
        for k, v in enumerate(data):
            if v["username"] == user and v['pin'] == pin:
                print("You will be missed, GOODBYE!!")
                delete = pd.read_csv("user_wallet.csv")
                delete.drop(k)
                delete.to_csv("user_wallet.csv", index=False)
                return "Deletion Successful"
            else:
                print("Invalid Details!!")
                return

    @staticmethod
    def save_data(data):
        with open('user_data.csv', "w+") as ft:
            ft.writerow(data)
            return "Successfully Saved"

    @staticmethod
    def get_csv_data():
        with open('user_data.csv', 'r') as csv_file_text:
            data = csv.DictReader(csv_file_text)
            return list(data)

    @property
    def get_user_wallet_balance(self):
        return self.wallet_balance

    @property
    def get_user_wallet_address(self):
        return self.wallet_address


u1 = User().create_user("Olawale", "Obo", "Ola")
# # u2 = User('Jenny Doe',  '19371564761', 20000)
# value = 7513ZSW
print(u1)
w1 = Wallet().deposit_to_self(30, 79150)
# print(u2.balance)
# User.transfer(u1, u2, 10)
# print(u1.balance)
# print(u2.balance)
