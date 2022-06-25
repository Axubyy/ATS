import random


# def password_generator():
#     alphabets = ['a','b','c',
#     'd','e', 'f','g', 'h','i','j','k','l',
#     'm','n','o','p','q']
#     return  "".join(list(alphabets[0].upper())+(random.sample(alphabets,8))) + str(random.randint(10,100))


# print(password_generator())


def authenticate():
    first_name = input("Please Input your first name: ")
    lastname =   input("Please Input your last name: ")
    name_characters = list(first_name + lastname)

    username = "".join(list(name_characters[0:4]) + list(lastname[0:5]))

    user_detail = {
        "firstname":first_name,
        "lastname": lastname,
        "username" :username
    }
    return user_detail

print(authenticate())