# arr = ["apple", "guava", "orange", "tomatoes", "watermelon"]

# arr2 = arr.copy()

# print(arr[::-2])

# item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

price_dict = {}
# for i, j in enumerate(listed_arr):
#     print(i)
#     print(j)
print(old_price.items())
# for (item, value) in old_price.items():
#     print(f"{item}:{value}")

for (item, value) in enumerate(old_price.items()):
    print(f"{item}:{value}")

dollar_to_pound = 0.76
new_price = {item: value *
             dollar_to_pound for (item, value) in old_price.items()}
# print(new_price)
