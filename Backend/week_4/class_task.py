import csv


class User:
    def save_data(self,data):
        with open('csv_user_data.csv', "w+") as ft:
            ft.write(f"{data}")

    def get_csv_data():
        with  open('csv_user_data.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)
    
    
    
    
    def __init__(self) -> None:
      

    def create_user(self,firstname,lastname,username,password):
        
        user_data = {
            "firstname":firstname,
            "lastname":lastname,
            "username":username,
            "password":password
        } 
        
        self.save_data(user_data)
        
        return


    def delete(self,username,firstname):
        users_data = self.get_csv_data()
        for user in users_data:
                if user["username"] == username & user["firstname"] == firstname:
                    del user





class Wallet(User,):
    def __init__(self,address,balance) -> None:
        super.__init__(firstname,lastname,username,password):
        self.address = address
        self.balance = balance

        




class  Transaction:
    def __init__(self,_balance = 2000) -> None:
        self._balance = _balance

    def deposit_to_self(self, amount):
        self._balance += amount
    def deposit_to_others(self, amount, target_account_num):
        # Implicitly testing for valid account number
        if self.get_balance() > self._balance:
            self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def transfer(self, other, amount_out):
        self.withdraw(amount_out)
        other.deposit(amount_out)

    def log_transaction(self):

