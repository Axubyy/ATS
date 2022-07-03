# import pandas
import csv
def get_data():
        with open("user_data.csv", "r") as y:
            reader = csv.DictReader(y)
            # print(reader)
            # print(list(reader))
            for (i,k) in enumerate(list(reader)):
                print(i,k)
            return list(reader)
def delete_user():
        data = get_data()
        user = input("kindly input your username")
        pin = input("kindly input your pin")
        for k, v in enumerate(data):
            if v["username"] == user and v['pin'] == pin:
                print("You will be missed, GOODBYE!!")
                # delete = pandas.read_csv("user_wallet.csv")
                # delete.drop(k)
                # delete.to_csv("user_data.csv", index=False)
                return "Deletion Successful"
            else:
                print("Invalid Details!!")
                sys.exit()

print(delete_user())
