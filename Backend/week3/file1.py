def authenticate():
    first_name = input('Hello!  please enter your first name: ')
    last_name = input("Niceee!  please enter your last name: ")
    user_name = input("Alright choose a username: ")
    password = input(f"One last thing  {first_name}, please choose a password: ")
    password_confirm = input("Type password again to confirm: ")
    if password == password_confirm:
        user_data = [{
            first_name: first_name,
            last_name: last_name,
            user_name: user_name,
            password: password,
            password_confirm: password_confirm
        }]
        with open(f"{user_name}.txt", "w+") as ft:
            ft.write(f"{user_data}")
    else:
        print("Passwords don't match, Please check again")
        return
    return ft.readline(f"{user_data}.txt")


print(authenticate())
