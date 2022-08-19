
from decimal import Decimal
import csv
from email import header


class_data = {
    "ahmad@gmail.com": {'first_name': 'Ahmad', 'last_name': 'Sharafudeen', 'day_month': '9-3', 'attendance': 11, 'height': 160,
                        'weight': 55, 'age': 25},
    "awwal@gmail.com": {'first_name': 'Awwal', 'last_name': 'Adeleke', 'day_month': '4-6', 'attendance': 11, 'height': 165,
                        'weight': 61, 'age': 21},
    'Abdulwali@gmail.com': {'first_name': 'Abdulwali', 'last_name': 'Tajudeen', 'day_month': '10-12', 'attendance': 11, 'height': 170,
                            'weight': 52, 'age': 24},
    'abraham@gmail.com': {'first_name': 'Abraham', 'last_name': 'Adekunle', 'day_month': '2-6', 'attendance': 11, 'height': 157,
                          'weight': 70, 'age': 28},
    'yusuff@gmail.com': {'first_name': 'Yusuf', 'last_name': 'Oyedele', 'day_month': '22-7', 'attendance': 11, 'height': 172,
                         'weight': 64, 'age': 26},
    'adebusola@gmail.com': {'first_name': 'Adebusola', 'last_name': 'Adeyeye', 'day_month': '14-8', 'attendance': 11, 'height': 131,
                            'weight': 58, 'age': 24},
    'basheer@gmail.com': {'first_name': 'Basheer', 'last_name': 'Balogun', 'day_month': '19-11', 'attendance': 11, 'height': 141,
                          'weight': 48, 'age': 22},
    'abdullahi@gmail.com': {'first_name': 'Abdullahi', 'last_name': 'Salaam', 'day_month': '13-9', 'attendance': 11, 'height': 156,
                            'weight': 68, 'age': 19},
    'faith@gmail.com': {'first_name': 'Faith', 'last_name': 'Adeosun', 'day_month': '17-4', 'attendance': 11, 'height': 141,
                        'weight': 56, 'age': 22},
    'lukman@gmail.com': {'first_name': 'Lukman', 'last_name': 'Abisoye', 'day_month': '15-2', 'attendance': 11, 'height': 169,
                         'weight': 59, 'age': 27},
    'toluwanimi@gmail.com': {'first_name': 'Toluwanimi', 'last_name': 'Ogunbiyi', 'day_month': '12-7', 'attendance': 11, 'height': 181,
                             'weight': 53, 'age': 23},
}


class Student:
    def __init__(self) -> None:
        self.student_data = class_data

    def sign_up(self):
        data = self.read_data
        firstname = input("Input your firstname:")
        lastname = input("Input your lastname:")
        email = input("Input your email:")
        password = input("Input your password:")

        user = {
            'firstname': firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
        }
        self.student_data[email] = user

    def get_max_age(self):
        max_age = 0

        for student in self.student_data.keys():
            if student['age'] > max_age:
                max_age = student['age']
        return max_age

    def get_min_age(self):
        min_age = Decimal(0)
        age_list = []
        for student in self.student_data.keys():
            age_list.append(student['age'])

        # agelist = [student['age'] for student in]
        # or even sort

        min_age = min(age_list)
        return min_age

    def average_age(self):
        ages = []
        sumST = 0
        for student in self.student_data.keys():
            sumST += student['age']
            ages.append(student['age'])

        avg = sum(ages)/len(ages)
        return avg

    def get_month_of_birth(self):
        pass


class LoginWithEmail:
    headers = ['firstname', 'lastname', 'username',
               'password', 'phone_number', 'address', 'dob', 'gender']

    def read_data(self):
        with open('user.csv') as file:
            handler = csv.Dictreader(file)
            return list(handler)

    def save_data(self, data):
        with open('user.csv', mode='w') as file:
            handler = csv.DictWriter(file, filename=header)

            handler.writerow(data)

    def __init__(self, email) -> None:
        self.first_name = class_data[email]['first_name']
        self.last_name = class_data[email]['last_name']

    def sign_up(self):
        data = self.read_data
        firstname = input("Input your firstname:")
        lastname = input("Input your lastname:")
        email = input("Input your email:")
        password = input("Input your password:")
