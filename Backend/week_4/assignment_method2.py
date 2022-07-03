import csv
from operator import ge
import random
import string




class Wallet:
    random_digits = string.digits
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    wallet_header = ["wallet_ID", "amount", "balance"]
   
    def __init__(self,wallet_balance = 1000)  -> None:
            self.wallet_balance = wallet_balance
            random_digits = string.digits
            upper_letters = string.ascii_uppercase
            # lower_letters = string.ascii_lowercase
            generate_wallet_address =  "".join(random.sample(random_digits,4)) + "".join(random.sample(upper_letters,3))
            self.wallet_address = generate_wallet_address
    



    @staticmethod
    def save_wallet_data(**args):
        with open("user_data.csv", "w", newline="\n") as wallet_file:
            writer = csv.DictWriter(wallet_file, fieldnames=Wallet.wallet_header)
            writer.writeheader()
            writer.writerow(**args)
        return "Registration Successful"
        
    @property
    def get_wallet_address(self):
        return self.wallet_address

class  Transaction:
    def __init__(self) -> None:
        self.address = Wallet.get_wallet_id()
        self._balance = User.get_user_balance()
    
    def deposit_to_self(self, amount,wallet_address):
        users_data = User.get_csv_data()
        for user in users_data:
            if user["wallet_address"] == wallet_address:
                user['wallet_balance'] += amount
                self._balance += amount

    def deposit_to_others(self, amount,user_account_num, target_account_num):
        user_data = User().get_csv_data()
        # Implicitly testing for valid account number
        if self.get_balance() > self._balance:
            self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def transfer(self,from_wallet_id,to_wallet_id, amount_out):
        self.withdraw(amount_out)
        self.deposit(amount_out)

    def log_transaction(self):
        pass

    def log_transaction(self,user_id, username):
        users_logs = self.get_transaction_data()
        for user_log in users_logs:
            if user_log["username"] == username & user_log["user_id"] == user_id:

                return

    @staticmethod
    def get_transaction_data():
         with  open('csv_user_transactions.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)
        


class User:

    random_digits = string.digits
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    pin_code  = "".join(random.sample(random_digits,5))
    wallet_address =  "".join(random.sample(random_digits,4)) + "".join(random.sample(upper_letters,3))
    
    user_header = ["firstname","lastname", "username","pin_code", "wallet_address","balance"]
    
    
   
    
    def __init__(self) -> None:
        self.account_balance = Wallet().wallet_balance
        # self.wallet_address = Wallet().wallet_address
        self.wallet = Wallet()
         

    def create_user(self,firstname,lastname,username):
        #implement as inputs
       
        
        user_data = {
            "firstname":firstname,
            "lastname":lastname,
            "username":username,
            "pin_code": User.pin_code,
            "wallet_address": User.wallet_address,
            "balance":1000
        } 
        
        print(f"Here are ,your ID, and your pin is {User.pin_code}, Dont disclose this!")

        with open("user_data.csv", "a", newline="\n") as user_file:
            writer = csv.DictWriter(user_file, fieldnames=User.user_header)
            # writer.writeheader()
            writer.writerow(user_data)
        return "Registration Successful"
        
        

    @staticmethod
    def save_data(data):
        with open('user_data.csv', "w+") as ft:
            ft.write(f"{data}")

    @staticmethod
    def get_csv_data():
        with  open('user_data.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)

    def delete_user(self,username,firstname):
        users_data = self.__class__.get_csv_data() #User.get_csv_data()
        
        for user in users_data:
                if user["username"] == username and user["firstname"] == firstname :
                    del user
                    
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
    @property
    def get_user_wallet_balance(self):
        return self.wallet_balance

    @property
    def get_user_wallet_address(self):
        return self.wallet_address
    
   
    





u1 = User().create_user("Ekene","Obo","Emmy")
# u2 = User('Jenny Doe',  '19371564761', 20000)
print(u1)
# print(u2.balance)
# User.transfer(u1, u2, 10)
# print(u1.balance)
# print(u2.balance)