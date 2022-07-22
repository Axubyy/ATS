import re


def move_elem_to_end(array: list, num: int):
    i = 0
    j = len(array)-1

    while j > i:
        left_idx = array[i]
        right_idx = array[j]

        while j > i and array[j] == num:
            j -= 1
        if array[i] == num:
            array[i], array[j] = array[j], array[i]
        i += 1

    return array


print(move_elem_to_end([2, 1, 3, 4, 2, 2, 2], 2))
