import csv


def authenticate():
    
    def check_is_str(input_str):
        if not input_str.strip().isalpha():
            print("Input Error")
        return input_str
    
    def password_check(passwd):
        if len(passwd) >= 8:
            return passwd
        else:
            print("Password must not be less than 8 characters")
            password_check(passwd)

    def signup():
        first_name = check_is_str(input('Hello!  please enter your first name: '))
        last_name = check_is_str(input("Nice!  please enter your last name: "))
        password = password_check(input(f"One last thing  {first_name}, please choose a password: "))
        confirm_password = password_check(input("Please Input Password again: "))
        if password == confirm_password:
            user_data = [{
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
                "confirm_password":confirm_password
            }]
            with  open('csv_user_data.csv', 'w') as csv_file_text:
                headers = [
                    "first_name", "last_name","password",
                "confirm_password"]
                handlers = csv.DictWriter(csv_file_text, fieldnames=headers)
                handlers.writeheader()
                handlers.writerows(user_data)
        else:
             print("Passwords dont match!")
             signup()

    def get_csv_data():
        with  open('csv_user_data.csv', 'r') as csv_file_text:
            return csv.DictReader(csv_file_text)

    def validate_info(data):
        for row in get_csv_data():
            if row[f"{data}"] == data:
                return True

        

    def signin():
        first_name = check_is_str(input('Hello!  please enter your first name: '))
        last_name = check_is_str(input("Nice!  please enter your last name: "))
        password = password_check(input(f"One last thing  {first_name}, please choose a password: "))
        for row in get_csv_data():
                if row["passeword"] ==  password:
                    print("You are logged In!")
                else:
                    print("Incorrect password")

    def welcome_to_home():
        print(" Welcome, Have an account, Signin please, else please Signup: Press 1 for Signin, 2 - Signup")
        signin_val = input(":")
        signup_val = input("")
        val = signin() if signin_val == 1 else signup()
        return val 
    welcome_to_home()


        





print(authenticate())
