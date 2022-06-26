def generate_list():
    list_of_num = [x for x in range(2,1000)]
    print(list_of_num)
    for num in list_of_num:
        list_length = len(list_of_num)
        p = 0
        while p < list_length:
            yield num 
        p+=1

def prime_number(num):
    isPrime = True
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
            return isPrime
        else:
            return isPrime

def prime_num_list():            
        prime_array = []
        for i in generate_list():
            isPrimeValue = prime_number(i)
            if isPrimeValue :
                prime_array.append(i)
                print(prime_array)
                return prime_array

print(prime_num_list())