# value = input('Choose a surname:')

# message = 'His name is Bolu'

# message = "His name is Bolu{}".format(value)
# print(message)

# ask for username and password and compare with your a set of username & password and confirm authentication

def open_account_or_create_PIN():
        firstName =  str(input('Please input your first name:'))
        lastName =  str(input('Please input your last name:'))

        print(f'Welcome {firstName}{lastName}')

        userName =  str(input('Please input your Username:'))
        password =  str(input('Please input your Password:'))
        userDetails  = {
                "name": userName, 
                "passwd": password
                }


        userName2 =  input('Please validate your Username:')
        password2 =  input('Please validate your Password:')

        if (userName2 != userDetails['name']) or (password2 != userDetails['passwd']):
            print('Ooops! Incorrect username or password. Please try again.')
        else:
            print('Yoo! you are logged in.')



