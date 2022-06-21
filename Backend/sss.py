import  csv


 
 def sign_in():
    first_name = input('Hello!  please enter your first name: ')
    last_name = input("Nice!  please enter your last name: ")
    password = input(f"One last thing  {first_name}, please choose a password: ")

    with  open('csv_user_data.csv', 'r') as csv_file_text:
        handler = csv.DictReader(csv_file_text)
        print(handler)
        for row in handler:
            print(handler)
