def smallest_difference(array1, array2):
    array1.sort()
    array2.sort()
    pointer1 = 0
    pointer2 = 0
    smallest_diff = float("inf")
    current_diff = float("inf")
    smallest_pair = []

    while pointer1 < len(array1) and pointer2 < len(array2):
        first_num = array1[pointer1]
        second_num = array2[pointer2]
        # current_diff
        # current_diff = abs(first_num - second_num)
        if first_num < second_num:
            current_diff = second_num - first_num
            pointer1 += 1
        elif second_num < first_num:
            current_diff = first_num - second_num
            pointer2 += 1
        elif second_num == first_num:
            return [first_num, second_num]

        if smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_pair = [first_num, second_num]
    return smallest_pair
