def product_sum(array):
    sum = 0
    M = 1
    for i in range(len(array)):
        is_num = True if type(array[i]) is int else False
        is_array = True if type(array[i]) is list else False
        if is_num:
            sum += array[i]
        elif is_array:
            M += 1
            sum += M * product_sum(array[i])
    return sum * M


def productSum(array, multiplier=1):
    sum = 0
    for elem in array:
        if type(elem) is list:
            sum += productSum(elem, multiplier+1)
        else:
            sum += elem
    return sum * multiplier
