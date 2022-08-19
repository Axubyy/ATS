# profile_data ={"basheer@gmail.com":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
#                 "abdullahi@gmail.com":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
#                 "faith@gmail.com":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
#                 "ahmad@gmail.com": {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
#                 "toluwanimi@gmail.com":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
#                 "awwal@gmail.com": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
#                 "abdulwali@gmail.com": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27,
#                 "birthday":
#                  {
#                     "day":8,
#                     "month": "Mar",
#                     }
#                     },
#                 "abraham@gmail.com": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
#                 "yusuff@gmail.com": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
#                 "adebusola@gmail.com": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
#                 "lukman@gmail.com": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}

# class UserProfile:

#     def __init__(self,data_dict):
#         self.data_dict = profile_data


#     def update_firstname_and_lastname(self,lastname_update,firstname_update,user_email):
#         for email in self.data_diprofile_data ={"basheer@gmail.com":{"first_name" :"Basheer", "last_name":"Balogun","attendance": 11,"height": 46, "weight": 23,"age":22, "birthday": {"day":8, "month": "april",}},
#                 "abdullahi@gmail.com":{"first_name" :"Abdullahi", "last_name":"Salam","attendance": 11,"height": 25, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
#                 "faith@gmail.com":{"first_name" :"Faith", "last_name":"Adeosun","attendance": 11,"height": 50, "weight": 23,"age":23, "birthday": {"day":8, "month": "Agu",}},
#                 "ahmad@gmail.com": {"first_name" :"Ahmad", "last_name":"Sharafudeen","attendance": 11,"height": 71, "weight": 23,"age":23, "birthday": {"day":8, "month": "July",}},
#                 "toluwanimi@gmail.com":  {"first_name" :"Toluwanimi", "last_name":"Ogunbiyi","attendance": 11,"height": 34, "weight": 24,"age":21, "birthday": {"day":8, "month": "Nov",}},
#                 "awwal@gmail.com": {"first_name" :"Awwal", "last_name":"Adeleke","attendance": 11,"height":49 ,"weight": 23,"age":23, "birthday": {"day":8, "month": "Dec",}},
#                 "abdulwali@gmail.com": {"first_name" :"Abdulwali", "last_name":"Tajudeen","attendance": 11,"height": 78, "weight": 23,"age":27,
#                 "birthday":
#                  {
#                     "day":8,
#                     "month": "Mar",
#                     }
#                     },
#                 "abraham@gmail.com": {"first_name" :"Abraham", "last_name":"Adekunle","attendance": 11,"height": 65, "weight": 23,"age":23, "birthday": {"day":8, "month": "May",}},
#                 "yusuff@gmail.com": {"first_name" :"Yusuff", "last_name":"Oyedele","attendance": 11,"height": 52, "weight": 23,"age":23, "birthday": {"day":8, "month": "Oct",}},
#                 "adebusola@gmail.com": {"first_name" :"Adebusola", "last_name":"Adeyeye","attendance": 11,"height": 43, "weight": 23,"age":26, "birthday": {"day":8, "month": "Feb",}},
#                 "lukman@gmail.com": {"first_name" :"Lukman", "last_name":"Abisoye","attendance": 11,"height": 35, "weight": 54,"age":29, "birthday": {"day":4, "month": "Jan",}}}

# class UserProfile:

#     def __init__(self,data_dict):
#         self.data_dict = profile_data


#     def update_firstname_and_lastname(self,lastname_update,firstname_update,user_email):
#         for email in self.data_dict:
#             if user_email == email:
#                 self.data_dict[user_email]["first_name"] = firstname_update
#                 self.data_dict[user_email]["lastname"] = lastname_update
#             return


#     def list_of_fullnames(self):
#         for email in self.data_dict:
#             i =1
#             for (k,v) in enumerate(email):
#                 print(f"User name {i} is {k} {v}")
#                 i+=1
#         return


#     def add_profile(self,user_email,user_firstname,user_lastname,):
#         pass

#     def increase_attendance(self,user_email):
#         for email in self.data_dict:
#             if user_email == email:
#                 self.data_dict[user_email]["attendance"] +=1
#             return

#     def sort_by_month(self):
#         sorted_month_data = {}
#         for email in self.data_dict:
#             for birthday in email:
#                 for (k,v) in enumerate(birthday):
#                     if k in sorted_month_data.keys():

#                         sorted_month_data[k].update(self.data_dict[email])
#                         list(sorted_month_data.values()).append(k)
#                     else:
#                         sorted_month_data[k] = {self.data_dict[email]}ct:
#             if user_email == email:
#                 self.data_dict[user_email]["first_name"] = firstname_update
#                 self.data_dict[user_email]["lastname"] = lastname_update
#             return


#     def list_of_fullnames(self):
#         for email in self.data_dict:
#             i =1
#             for (k,v) in enumerate(email):
#                 print(f"User name {i} is {k} {v}")
#                 i+=1
#         return


#     def add_profile(self,user_email,user_firstname,user_lastname,):
#         pass

#     def increase_attendance(self,user_email):
#         for email in self.data_dict:
#             if user_email == email:
#                 self.data_dict[user_email]["attendance"] +=1
#             return

#     def sort_by_month(self):
#         sorted_month_data = {}
#         for email in self.data_dict:
#             for birthday in email:
#                 for (k,v) in enumerate(birthday):
#                     if k in sorted_month_data.keys():

#                         sorted_month_data[k].update(self.data_dict[email])
#                         list(sorted_month_data.values()).append(k)
#                     else:
#                         sorted_month_data[k] = {self.data_dict[email]}


# for x in range(-9, 10):
#     print(x*x)

Numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
Result = []
for list in Numbers:
    Squares = [Number ** 2 for Number in list if Number % 2 == 0]
    Result.extend(Squares)

print(Result)
print([x**2 for num in Numbers for x in num if x % 2 == 0])
