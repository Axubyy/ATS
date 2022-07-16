# import csv
# with open('user_data.csv', 'r') as file:

#     reader = csv.reader(file)
#     print(reader)
# for row in reader:
#     # print(row)

# data_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]

# # with open("new_file.csv", "w") as file:

# with open('innovators.csv', 'w',) as file:
#     writer = csv.writer(file)
#     print(writer)
#     writer.write
#     writer.writerows(data_list)

import csv

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
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
