import csv

with open('countries.csv', 'r', newline='') as csvfile:
    spam_reader = csv.DictReader(csvfile)
    for row in spam_reader:
        print(row)
        # if row['Year'] == 1999:
        # print(row['Year'])

        # print(row.items())

# with open('egg.csv', 'w+', newline='') as csvfile:
#     spam_writer = csv.writer(csvfile)
#     print(spam_writer)
# spam_writer.writerow(['Titles'] * 2 + ['Bakers'])
# spam_writer.writerow(['a', 'Lo Sa', 'Wonder'])
# spam_writer.writerow(['Spa', 'Lovely Spa', 'Wonderful Spam'])
# spam_writer.writerow(['well', 'Love', 'Spam'])

# username = ''
# user ={}
# with open('egg.csv','r') as file:
#     read_handler = csv.DictReader(file)
#     for key_elem in read_handler:
#         if key_elem['username'] ==  username.lower()
#             user = key_elem
#             break
#         print(f"User info{user}")
#     phone_number = input("gg")
#     address = input(";")
#     if not address:
#         address = username['address']
#     date_of_birth = input("Please input ")
#     if not date_of_birth:
#         date_of_birth = username['date_of_birth']
#     gender = input("Please input ")
#
#     if gender and phone_number:
#         with open('csv_file.csv','r') as modified_file:
#             modified_file_handler = csv.DictReader(modified_file)
#
#             user_info = []
#             for info in modified_file_handler:
#                 if info['username'] == username:
#                     info['phone_number'] ==phone_number
#                     info['address'] == address
#                     info['date_of_birth'] = date_of_birth
#                     info['gender'] = gender
#                     user_info.append(info)
#             with open('csv_file.csv','w') as  file2:
#                 file2_handler =csv.DictWriter(file2,fieldnames=headers)
#                 file2_handler.writeheader()
#                 for i in user_info:
#                     file2_handler.writerow(info)
#                 print('Updated Profile!')
