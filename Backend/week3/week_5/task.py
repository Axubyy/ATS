import random
random_list = [x for x in random.sample(range(1, 99), 20)]

random_dict = {x: y for x, y in random_list}

list_dict_values = list(random_list.values())


# for i,j in enumerate(list_dict_values):
#     duplicate_values = []
