def three_largest_num(array):
    # return sorted(array)[-3]
    three_largest_list = [None, None, None]
    for num in array:
        update_largest_num(three_largest_list, num)
    return three_largest_list


def update_largest_num(largest_list, num):
    if largest_list[2] is None or num > largest_list[2]:
        insert_num(largest_list, num, 2)
    elif largest_list[1] == None or num > largest_list[1]:
        insert_num(largest_list, num, 1)
    elif largest_list[0] == None or num > largest_list[0]:
        insert_num(largest_list, num, 0)


def insert_num(arr, num, idx):
    for i in range(idx+1):
        if i == idx:
            arr[i] = num
        else:
            arr[i] = arr[i+1]
