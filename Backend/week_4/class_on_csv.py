import pandas
import csv
# with open('./user_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     readerDict = csv.DictReader(file, delimiter=',')
#     line_count = 0
#     for row in reader:
#         if line_count == 0:
#             print(f"This is for the {row[0]}  and {row[1]}")
#             line_count += 1
#         else:
#             # for row2 in readerDict:
#             print(f"Welcome {row[0]} {row[1]} to our office today")
#     for row2 in readerDict:
#         print(row2)
#         sentence = f"{row2['firstname']} is the boss of {row2['lastname']}"
#         print(sentence)
#         print(row2["firstname"])

#     print(f" This guy {row2} is his first name")

data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]
             ]


# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# csv data
rows = [
    {'name': 'Albania',
     'area': 28748,
     'country_code2': 'AL',
     'country_code3': 'ALB'},
    {'name': 'Algeria',
     'area': 2381741,
     'country_code2': 'DZ',
     'country_code3': 'DZA'},
    {'name': 'American Samoa',
     'area': 199,
     'country_code2': 'AS',
     'country_code3': 'ASM'}
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()
    writer.writerows(rows)


# with open('innovators.csv', 'w',) as file:
#     writer = csv.writer(file, delimiter="|")
#     print(writer)
#     # writer.write()
#     writer.writerows(data_list)
df = pandas.read_csv('countries.csv')
print(df)
# df.to_csv('new_countries.csv')
