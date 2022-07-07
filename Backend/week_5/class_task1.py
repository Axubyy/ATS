import random
random_list = [x for x in random.sample(range(1, 99), 20)]
print(random_list)

random_dict = {y: y for  y in random_list}
print(random_dict)
list_dict_values = list(random_dict.values())
flipped_dict = {}
duplicate_nums = []
def check_duplicates(dic):
    for key,value in random_dict.items():
           # i = 1 if i not in duplicate_val_list else +1
            if value not in flipped_dict:
               
                flipped_dict[value] = [key]
            else:
                # print(key)
                flipped_dict[value].append(key)
                duplicate_nums.append(value)
    duplicates = []
    # print(flipped_dict)
    # print(duplicate_nums)
    for arr in flipped_dict.values():
        if len(arr) > 1:  
            duplicates = duplicates + arr
            # print(duplicates)
    print(f"The duplicate value(s) are {duplicate_nums} with the key(s){duplicates}")
        
    return   duplicates

check_duplicates(random_dict)
                # print(f"{i} has a duplicate"


# for i,j in enumerate(list_dict_values):
#     duplicate_values = []
