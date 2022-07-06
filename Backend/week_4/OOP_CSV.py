
import csv


class CsvProfileClass:
    headers = ['username', 'first_name', 'last_name', 'password', 'phone_number', 'date_of_birth']

    def __init__(self) -> None:
        pass
        # self.user_credential = self.signin()

    # # 1. After successful signup, it should prompt the user to signin.
    # 2  # . After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
    # 3.  # Edit profile should ask for more information like phone_number (required), address (optional), date of birth (
    # # optional) and gender (compulsory)

    def update_profile_prompt(self, user_credential):
        update_choice = input("Please update your Profile:"
                              "Choose action to perform"
                              "1 - Edit Profile"
                              "2- Change Password"
                              "3- Logout")
        if update_choice == 1:
            self.edit_profile(user_credential)
        elif update_choice == 2:
            self.change_password(user_credential)
        elif update_choice == 3:
            self.logout(user_credential)

    def signin(self, username, password):
        data = self.get_data()
        for profile in data:
            if profile['username'] == username and profile['password'] == password:
                print(f'Login successful')
                username = user_credential
                return username
            else:
                print(f"Invalid login credentials")

    user_credential = self.signin()
    update_profile_prompt()

    def validate_confirm_password(self, password, confirm_password):
        return password == confirm_password

    def get_data(self):
        with open('user_db.csv', 'r') as f:
            csv_file = csv.DictReader(f)
            return list(csv_file)

    def save_data(self, **kwargs):
        with open('user_db.csv', 'a', newline='\n') as f:
            csv_file = csv.DictWriter(f, fieldnames=headers)
            csv_file.writerow(kwargs)

    def change_password(self, username):
        new_password = self.get_password()
        user_data = self.get_data()
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

    def edit_profile(self, **kwargs):
        phone_number = get_phone_number()
        address = get_address()
        date_of_birth = "".join(get_date_of_birth().split("-"))
        gender = get_gender()
        headers2 = ['phone_number', 'address', 'date_of_birth', 'gender']
        # date_of_birth = str("".join(date_of_birth))
        self.update_data(kwargs)

    def signup(self, username, firstname, last_name, password, confirm_password):

        # Validation starts here
        if not self.validate_username(username):
            print(f"Error! Username: {username} already exists.")
            return False

        if not self.validate_confirm_password(password, confirm_password):
            print(f"Error! Password and confirm password are different")
            return False

        self.save_data(username=username, first_name=first_name, last_name=last_name, password=password)
        self.signin()

    def get_username():
        return input("Enter your username: ")

    def validate_username(self, username):
        data = self.get_data()
        for profile in data:
            if profile['username'] == username:
                return False
        return True

    # def get_first_name():
    #     return input("Enter first name: ")
    #
    # def get_last_name():
    #     return input("Enter last name: ")
    #
    # def get_password():
    #     return input("Enter password: ")
    #
    # def get_confirm_password():
    #     return input("Confirm password: ")
