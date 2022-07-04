import csv
import random
import string
import pandas as pd

from Backend.week_4.assignment_method2 import Transaction


class Wallet:
    def __init__(self)  -> None:
            random_digits = string.digits
            upper_letters = string.ascii_uppercase
            generate_wallet_address =  "".join(random.sample(random_digits,4)) + "".join(random.sample(upper_letters,3))
            self.wallet_address = generatengo_wallet_address
            


    @property
    def get_wallet_address(self):
        return self.wallet_address
        _
    def deposit_to_self(self, amount,wallet_address,pin_code):
        user_data = User().user_data_list
        for d in user_data:
            if d["wallet_addresses"] == wallet_address:
                d["balance"] += amount
                d["deposits"] += 1 if d["deposits"]  else 1
                print(f"You have Successfully deposited {amount} to your account")
                return
            
                
                
    
    def debit_wallet(wallet_address,amount):
        user_data = User().user_data_list
        for user in user_data:
            if user["wallet_addresses"] == wallet_address:
                user["balance"] -= amount
                user["debits"] += 1 if user["debits"]  else 1
                print(f"You have been debited the sum of {amount} to your account")
                return
            # if user["wallet_address"] == wallet_address:
            #     Wallet.save_wallet_data(amounts=amount,wallet_addresses=wallet_address,balances=int(d["balances"])+amount,deposits=1,debits=None)
            #     # Wallet.save_wallet_data(amounts=amount,wallet_addresses=wallet_address,balances=int(d["balances"])+amount,deposits=None,debits=1)
    
    def credit_wallet(self,wallet_address,amount):
        user_data = User().user_data_list
        for user in user_data:
           if user["wallet_addresses"] == wallet_address:
               user["balance"] -= amount
               user["debits"] += 1 if user["debits"] else 1
               print(
                   f"You have been credited the sum of {amount} to your account")
               return
    def transfer(self,from_wallet_address,to_wallet_address, amount_out):
        user_data = User().user_data_list
        for user in user_data:
            if from_wallet_address or to_wallet_address in user:


        # for k,v in user_data:
        #     if v["wallet_addresses"] == from_wallet_address and v["balance"] > amount_out:
        #         Wallet.debit_wallet(from_wallet_address,amount_out)
        #     if v["wallet_address"] == to_wallet_address:
        #         Wallet.credit_wallet(to_wallet_address,amount_out)



    # @staticmethod
    # def save_wallet_data(*args):

    #     # with open("wallet_data.csv", "w", newline="\n") as wallet_file:
    #     #     writer = csv.DictWriter(wallet_file, fieldnames=Wallet.wallet_header)
    #     #     writer.writeheader()
    #     #     writer.writerow(args)
    #     return "Registration Successful"
        
  
class  Transaction:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def log_transaction(self):
        user_data = User().user_data_list
        for user in user_data:
            [print(key,':',value) for key, value in user]
            return


        # df = pd.read_csv("wallet_data.csv")
        # df.head()
        # pd.options.display.max_columns = len(df.columns)
       

    # @staticmethod
    # def get_wallet_data():
    #      with  open('wallet_data.csv', 'r') as wallet_file_text:
    #         data = csv.DictReader(wallet_file_text)
    #         return list(data)
        


class User(Wallet,Transaction):

    random_digits = string.digits
    pin_code  = "".join(random.sample(random_digits,5))
    
    def __init__(self,firstname,lastname,username,pin_code,wallet_address,balance) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.pin_code = User.pin_code
        self.wallet_address = Wallet.get_wallet_address(),
        self.balance = 0
        self.user_data_list = []
        super().__init__()
                
        # self.account_balance = Wallet().wallet_balance
        # self.wallet_address = Wallet().wallet_address
        # self.wallet = Wallet()
         
    
    def save_user(self):
        

        user_data = {
            "firstname":self.firstname,
            "lastname":self.lastname,
            "username":self.username,
            "pin_code": self.pin_code,
            "wallet_address": self.wallet_address,
            "balance":self.balance
        } 
        self.user_data_list.append(user_data)
    #     print(f"Here are ,your ID, and your pin is {User.pin_code}, Dont disclose this!")
        print(f"Your private pin code is {self.pin_code}")
    #     with open("user_data.csv", "a", newline="\n") as user_file:
    #         writer = csv.DictWriter(user_file, fieldnames=User.user_header)
    #         # writer.writeheader()
    #         writer.writerow(user_data)
        return "User Saved Successfully"
        
    def delete_user(self,user_firstname,pin_code):
        user_data = self.user_data_list
        user = input("kindly input your username")
        pin = input("kindly input your pin")
        for data in user_data:
            if data["firstname"] == user_firstname and data['pin_code'] == pin_code:
                print("You will be missed, GOODBYE!!")
                del data
                return "Deletion Successful"
            else:
                print("Invalid Firstname or Pin code!!")
                return 

    # @staticmethod
    # def save_data(data):
    #     with open('user_data.csv', "w+") as ft:
    #         ft.writerow(data)
    #         return "Successfully Saved"

    # @staticmethod
    # def get_csv_data():
    #     with  open('user_data.csv', 'r') as csv_file_text:
    #         data = csv.DictReader(csv_file_text)
    #         return list(data)
                    
    # @property
    # def get_user_wallet_balance(self):
    #     return self.wallet_balance

    # @property
    # def get_user_wallet_address(self):
    #     return self.wallet_address
    
   
    





u1 = User().create_user("Olawale","Obo","Ola")
# # u2 = User('Jenny Doe',  '19371564761', 20000)
# value = 7513ZSW
print(u1)
w1 = Wallet().deposit_to_self(30,79150)
# print(u2.balance)
# User.transfer(u1, u2, 10)
# print(u1.balance)
# print(u2.balance)