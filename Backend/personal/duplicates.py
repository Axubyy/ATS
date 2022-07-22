a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
duplicate_values = {}

for val in a:
    if val in duplicate_values:
        duplicate_values[val] += 1
    else:
        duplicate_values[val] = 1

print([x for x, y in duplicate_values.items() if y > 1])
