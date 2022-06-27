def sieve_of_eratosthenes(limit):
    # limit = 999
    prime_container = [1 for _ in range(0, limit + 1)]
    prime_container[0], prime_container[1] = 0, 0
    primes = []
    print(prime_container)
    for (position, isPrime) in enumerate(prime_container):
        print(position, isPrime)
        if isPrime == 1:
            yield position
            for val in range(position * position, limit, position):
                prime_container[val] = 0
                primes.append(isPrime)
    #print(primes)
    # print(prime_container)
    return prime_container


print(sieve_of_eratosthenes(20))
