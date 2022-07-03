
# Message List
# Profile picture of Abraham Graham Adekunle.Message by Abraham Graham Adekunle
# Abraham Graham Adekunle17:28
# Text
import csv
# import pandas
import random
import string
import sys
class User:
    for_pin = string.digits
    for_id = string.ascii_uppercase
    head_king = ["Firstname", "Middlename", "Lastname", "username", "phone number", "wallet_ID", "pin", "balance"]
    head_wallet = ["wallet_ID", "Amount", "Balance"]
    def __init__(self):
        self.field = {}
    @staticmethod
    def get_data():
        with open("user_wallet.csv", "r") as y:
            reader = csv.DictReader(y)
            return list(reader)
    def user_registration(self):
        pin = "".join((random.sample(User.for_pin, 5)))
        wallet_id = "".join((random.sample(User.for_id, 3))) + "".join((random.sample(User.for_pin, 5)))
        self.field["Firstname"] = User.validate_firstname(self)
        self.field["Middlename"] = User.validate_middlename(self)
        self.field["Lastname"] = User.validate_lastname(self)
        self.field["username"] = User.validate_username(self)
        self.field["phone number"] = User.validate_phone(self)
        self.field["wallet_ID"] = wallet_id
        self.field["pin"] = pin
        self.field["balance"] = 0
        print(f"Here are ,your ID , {wallet_id}, and your pin {pin}, dont tell anyone")
        with open("user_wallet.csv", "a", newline="\n") as x:
            writer = csv.DictWriter(x, fieldnames=User.head_king)
            # writer.writeheader()
            writer.writerow(self.field)
        return "Registration Successful"
    def delete_user(self):
        data = User.get_data()
        user = input("kindly input your username")
        pin = input("kindly input your pin")
        for k, v in enumerate(data):
            if v["username"] == user and v['pin'] == pin:
                print("You will be missed, GOODBYE!!")
                delete = pandas.read_csv("user_wallet.csv")
                delete.drop(k)
                delete.to_csv("user_wallet.csv", index=False)
                return "Deletion Successful"
            else:
                print("Invalid Details!!")
                sys.exit()
    def validate_firstname(self):
        first_name = input("kindly input your firstname\n")
        if first_name.isalpha():
            return first_name
        print("invalid firstname")
        return User.validate_firstname(self)
    def validate_lastname(self):
        last_name = input("kindly input your lastname\n")
        if last_name.isalpha():
            return last_name
        print("invalid lastname")
        return User.validate_lastname(self)
    def validate_middlename(self):
        middlename = input("kindly input your middlename\n")
        if middlename.isalpha():
            return middlename
        print("invalid firstname")
        return User.validate_middlename(self)
    def validate_username(self):
        user_name = input("kindly input your username \n")
        if len(user_name) > 5:
            return user_name
        print("invalid username")
        return User.validate_username(self)
    def validate_phone(self):
        p_number = input(
            'Kindly type the new phone number , (add your country code and omit the first zero in your phone number) \n')
        if len(p_number) == 14 and p_number.startswith('+'):
            return p_number
        return User.validate_phone(self)
class Wallet(User):
    # def __init__(self, field):
    # super().__init__(field)
    # self.username = username
    # self.pin = pin
    def fund_wallet(self):
        amount = int(input("kindly input the amount you will like to add\n"))
        if amount < 0:
            print("invalid amount")
            sys.exit()
        data = User.get_data()
        wallet = input("Kindly input your Wallet ID\n")
        pin = input("kindly input your pin\n")
        for k, x in enumerate(data):
            if wallet == x["wallet_ID"] and pin == x["pin"]:
                print("login details, CORRECT!")
                Wallet.write_wallet(wallet_ID=wallet, Amount=amount, Balance=(int(x["balance"]) + amount))
                return "successful"
            else:
                print("invalid details")
                sys.exit()
    @staticmethod
    def write_wallet(**kwargs):
        with open("wallet.csv", "a", newline="\n") as z:
            writer = csv.DictWriter(z, fieldnames=User.head_wallet)
            # writer.writeheader()
            writer.writerow(kwargs)
    def get_balance(self):
        wallet = input("Kindly input your Wallet ID\n")
        pin = input("kindly input your pin\n")
        data = User.get_data()
        wall_data = Wallet.read_wallet()
        for x in data:
            if wallet == x["wallet ID"] and pin == x["pin"]:
                print("valid details")
                for y in wall_data:
                    if y["wallet_ID"] == wallet:
                        return y["balance"]
            else:
                return "Error! Invalid details"
    @staticmethod
    def read_wallet():
        with open("wallet.csv" "r") as x:
            reader = csv.DictReader(x)
            return list(reader)
Wallet().fund_wallet()