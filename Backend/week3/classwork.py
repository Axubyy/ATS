import csv
import re


def authenticate():
    def check_is_digit(input_str):
        if input_str.strip().isdigit():
            return input_str

    def check_is_str(input_str):
        if input_str.strip().isalpha():
            return input_str



    def check_is_M_or_S(input_str):
        if input_str == "M" or "S":
            return input_str

    first_name = check_is_str(input('Hello!  please enter your first name: '))
    last_name = check_is_str((input("Nice!  please enter your last name: ")))
    def is_email(input_str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, input_str):
            return input_str
    email = is_email(input("Please input your email"))
    marital_status = check_is_M_or_S(input(' Your Marital status. S for single, M for Marital: '))
    age = check_is_digit(input("Please input your age: "))
    occupation = check_is_str(input("What is your occupation: "))
    password = input(f"One last thing  {first_name}, please choose a password: ")
    headers = ["firstname", "lastname", "email", "marital_status", "age", "occupation", "password"]

    user_data = [{
        first_name: first_name,
        last_name: last_name,
        email: email,
        marital_status: marital_status,
        age: age,
        occupation: occupation,
        password: password
    }]

    with  open('csv_user_data.csv', 'w') as csv_file_text:
        handlers = csv.DictWriter(csv_file_text, fieldnames=headers)
        handlers.writeheader()
        handlers.writerows(user_data)

    def search():

        search_value = input(" Please input search term :")
        search_header = input(" What are you searching for ? A firstname, lastname , age etc :  ")
        with open('csv_user_data.csv', 'r') as csv_file:
            read_handler = csv.DictReader(csv_file)
            for row in read_handler:
                if search_header in row or search_value in row:
                    print(f"{search_header[search_value]} was found  in {search_header}")
                    return row
                print(f"Your search {search_value} was not found in our database")
        return

    print(" Looking for something, Would you lke to search?")
    input_value = input(" Y for yes, N for No: ")
    if input_value == "Y":
        print(search())


print(authenticate())
