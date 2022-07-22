# food = ["Akpu", "fufu", "rice", "beans"]
# num = [1, 3, 4, 5, 3, 7]

# food_dict = zip(num, food)
# foody = {k: v for k, v in zip(num, food)}
# for k, v in enumerate(dict(zip(num, food)).items()):
#     # for m, n in dict(v):
#     print(f"{v}")
#     print()
# # print(foody)
# listed = list(zip('abcdefg', range(3), range(4)))


# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

# new_dict_1 = {k: ('old' if v % 2 == 0 else 'norms')
#               for (k, v) in original_dict.items()}
# print(new_dict_1)

# test_list = [1, 6, 3, 5, 3, 4]

# result = any(item not in test_list for item in test_list)
# print("Does string contain any list element : " + str(bool(result)))
keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']

dict = {}
for i in range(len(keys)):
    dict[values[i]] = keys[i]

print(dict)
