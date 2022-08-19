

def check_for_two_sums(arr, target_sum):
    arr = sorted(arr)
    start_index = 0
    end_index = len(arr)-1
    i = 0
    sum_arr = []
    while i < len(arr):
        if arr[start_index] + arr[end_index] == target_sum:
            sum_arr.append(arr[start_index], arr[end_index])

        elif arr[start_index] + arr[end_index] > target_sum:
            start_index += 1
            i += 1
            print(end_index)
        elif arr[start_index] + arr[end_index] < target_sum:
            end_index -= 1
            i += 1
    print(sum_arr)
    print(i)

    print(start_index)
    return sum_arr

# second implementation


def check_for_sum(arr, target_sum):
    hash_table = {}
    for num in arr:
        # y = target_sum - num    or
        if target_sum - num in hash_table:
            return [target_sum-num, num]
        else:
            hash_table[num] = True
        print(hash_table)
    return []

    # for i in range(len(arr)):
    #     x = arr[i]
    #     y = arr[i+1]
    #     for x in hash_table:
    #         if target_sum - x == y:
    #             hash_table[x] = True
    #             hash_table[y] = True
    #         elif target


print(check_for_two_sums([1, 3, 4, 5, 6, 7, ], 9))
