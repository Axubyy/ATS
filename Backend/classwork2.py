import csv


def authenticate():
    
    def check_is_str(input_str):
        if not input_str.strip().isalpha():
            print("Input Error")
        return input_str
    
    def password_check(paswd):
        if len(paswd) < 8:
            print("Password must not be less than 8 characters")
        return paswd

    first_name = check_is_str(input('Hello!  please enter your first name: '))
    last_name = check_is_str(input("Nice!  please enter your last name: "))
    password = password_check(input(f"One last thing  {first_name}, please choose a password: "))
    confirm_password = password_check(input("Please Input Password again: "))
    if password != confirm_password:
        print("Passwords dont match!")

    user_data = [{
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "confirm_password":confirm_password
    }]

    with  open('csv_user_data.csv', 'w') as csv_file_text:
        headers = ["first_name", "last_name", "password","confirm_password"]
        handlers = csv.DictWriter(csv_file_text, fieldnames=headers)
        handlers.writeheader()
        handlers.writerows(user_data)

    def get_csv_data():
        with  open('csv_user_data.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)


    def signin():
        first_name = check_is_str(input('Hello!  please enter your first name: '))
        last_name = check_is_str(input("Nice!  please enter your last name: "))
        password = password_check(input(f"One last thing  {first_name}, please choose a password: "))
        for row in get_csv_data:
                if row["password"] ==  password:
                    print("You are logged In!")
                else:
                    print("Incorrect password")

    def welcome_to_home():
        print(" Welcome, Have an account, signin else, please signup ")
        signin_val = input("1 - Signin")
        signup_val = input("2 - Signp")
        val = signin() if signin_val == 1 else authenticate()
        return val 


        





print(authenticate())
