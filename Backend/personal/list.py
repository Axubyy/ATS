def list_sum(arr: list):
    # total = 0
    # for i in range(len(arr)):
    #     total += arr[i]
    # return total, i
    size = len(arr)
    index = 0
    total = 0

    while index < size:
        total = total + arr[index]
        index+1
    return total


print(list_sum([28, 3, 4, 6, .2, 40]))


def searchVal(arr, val):
    isPresent = False
    # for i in range(len(arr)):
    #     if val == arr[i]:
    #         isPresent = True
    #     else:
    #         isPresent = False
    # return isPresent
    index = 0
    size = len(arr)
    while index < size:
        if val == arr[index]:
            isPresent = True
        else:
            isPresent = False
        index+1
    return isPresent
