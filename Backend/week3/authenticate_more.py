import csv

# 1. After successful signup, it should prompt the user to signin.
2  # . After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
3.  # Edit profile should ask for more information like phone_number (required), address (optional), date of birth (
# optional) and gender (compulsory)

headers = ['username', 'first_name', 'last_name', 'password']
new_headers2 = ['username','first_name', 'last_name', 'password', 'phone_number', 'date_of_birth']


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


def update_profile_prompt():
    update_choice = input("Please update your Profile:"
                          "Choose action to perform"
                          "1 - Edit Profile"
                          "2- Change Password"
                          "3- Logout")
    if update_choice == 1:
        edit_profile(user_credential)
    elif update_choice == 2:
        change_password(user_credential)
    elif update_choice == 3:
        logout(user_credential)


def signin():
    username = get_username()
    password = get_password()

    data = get_data()
    for profile in data:
        if profile['username'] == username and profile['password'] == password:
            print(f'Login successful')
            username = user_credential
            return username
        else:
            print(f"Invalid login credentials")


user_credential = signin()
update_profile_prompt()


def change_password(username):
    new_password = get_password()
    user_data = get_data()
    for row in user_data:
        if row["username"] == username:
            # line_number = __newline
            with open('csv.csv', 'a') as file:
                file_handler = csv.DictWriter(file)
                file_handler.writerow([])
                user_info_ = row
                # [row for row in user_data if ]
            # old_password = input("please input old password")
            # new_password = input("Please Input new password")
            save_data()


def logout(user):
    user = None
    print(f"You have successfully logged out of your account!")
    return


def validate_phone_gender(value):
    return value if value else validate_phone_gender(value)


def get_phone_number():
    return input("Enter your phone number (this is required!): ")


def get_address():
    return input("Enter your address: ")


def get_gender():
    return input(" Please select your gender: ")


def get_date_of_birth():
    return input("Enter your date of birth: ")


def gender_check(user_gender):
    if user_gender not in ['M', 'F']:
        print(" Gender must be F for Female or M,Male")
        return get_gender(user_gender)
    return user_gender


def update_data():
    pass


def edit_profile():
    phone_number = get_phone_number()
    address = get_address()
    date_of_birth = "".join(get_date_of_birth().split("-"))
    gender = get_gender()
    headers2 = ['phone_number', 'address', 'date_of_birth', 'gender']
    # date_of_birth = str("".join(date_of_birth))
    update_data()


def signup():
    username = get_username()
    first_name = get_first_name()
    last_name = get_last_name()
    password = get_password()
    confirm_password = get_confirm_password()

    # Validation starts here
    if not validate_username(username):
        print(f"Error! Username: {username} already exists.")
        return False

    if not validate_confirm_password(password, confirm_password):
        print(f"Error! Password and confirm password are different")
        return False

    save_data(username=username, first_name=first_name, last_name=last_name, password=password)
    signin()


def get_username():
    return input("Enter your username: ")


def validate_username(username):
    data = get_data()
    for profile in data:
        if profile['username'] == username:
            return False
    return True


def get_first_name():
    return input("Enter first name: ")


def get_last_name():
    return input("Enter last name: ")


def get_password():
    return input("Enter password: ")


def get_confirm_password():
    return input("Confirm password: ")


def validate_confirm_password(password, confirm_password):
    return password == confirm_password


def get_data():
    with open('user_db.csv', 'r') as f:
        csv_file = csv.DictReader(f)
        return list(csv_file)


def save_data(**kwargs):
    with open('user_db.csv', 'a', newline='\n') as f:
        csv_file = csv.DictWriter(f, fieldnames=headers)
        csv_file.writerow(kwargs)


def main():
    option = input("Enter 1 to signup or 2 to signin (Default is 'Sign-In'): ")
    if option == '1':
        signup()
    else:
        signin()


if __name__ == "__main__":
    main()
