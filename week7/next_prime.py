def is_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True

def next_prime(N):
    while True:
        N += 1
        if is_prime(N) == True:
            return N

def next_twin_prime(N):
    while True:
        prime1 = next_prime(N)
        prime2 = next_prime(prime1)
        if prime2 - prime1 == 2:
            return (prime1, prime2)
        N = prime1
    # Return the least twin prime number which is more than N
    # twin prime numbers are 2 prime numbers differed by 2. For example -> (11 and 13) or (41 and 43).

exec(input().strip())

