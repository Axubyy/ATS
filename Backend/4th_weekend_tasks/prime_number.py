def generate_list():
    print("welcome")
    list_of_num = [x for x in range(2, 1000)]
    print(list_of_num)
    for num in list_of_num:
        while True:
            yield num


def prime_number(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            return isPrime
        else:
            return isPrime


def prime_num_list():
    prime_array = []
    print("welcome")
    for i in generate_list():
        isPrimeValue = prime_number(i)
        if isPrimeValue:
            prime_array.append(i)
            print(prime_array)
            return prime_array


print(prime_num_list())
# row, col = list(map(int, input("Enter row and column numbers to fix spot (with space(s) in between): ").split()))
# print(row,col)
