def prime_using_sqrt(limit):
    # limit = 999
    prime_container = [1 for _ in range(0, limit + 1)]
    prime_container[0], prime_container[1] = 0, 0
    primes = []
    print(prime_container)
    for i in range(2, int(limit ** 0.5) + 1):
        for j in range(2*i, limit+1, i):
            prime_container[j] = 0
        print(prime_container)
    print(prime_container)
    return prime_container


print(prime_using_sqrt(20))
