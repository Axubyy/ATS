# Use a list to solve the following problem:
# Read in 20 numbers. As each number is read, print
# it only if it is not a duplicate of a number already read.


import random
import  string

# def not_duplicate():
#     list = [x for x in range(0,20)]
#     print(list)
alpha_keys = list(string.ascii_lowercase)
alpha_keys = alpha_keys[:20]
# num_values = random.sample(range(1,99),20)
num_values = [1,2,3,4,5,5,6,6,7,8,9,10,11,12,13,14,15,16,17,18,]

num_dict = dict(zip(alpha_keys,num_values))
print(num_dict)
flipped_dict = {}
duplicate_nums = []
def check_for_duplicate():
        for key,value in num_dict.items():
           # i = 1 if i not in duplicate_val_list else +1
            if value not in flipped_dict:
               
                flipped_dict[value] = [key]
            else:
                print(key)
                flipped_dict[value].append(key)
                duplicate_nums.append(value)
        duplicates = []
        print(flipped_dict)
        print(duplicate_nums)
        for arr in flipped_dict.values():
            print(arr)
            if len(arr) > 1:  
                duplicates = duplicates + arr
                print(duplicates)
        print(f"The duplicate value(s) are {duplicate_nums} with the key(s){duplicates}")
            
        return   duplicates
                # print(f"{i} has a duplicate")
                # return i
check_for_duplicate()
# print(not_duplicate())
# D = {x: x * 2 for x in range(1, 100)}
# print(len(D))
# for i in range(0, random.randint(1, 99)):
#     i = i + 1
