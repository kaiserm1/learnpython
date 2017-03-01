# What is the largest prime factor of the number 600851475143?

number = 600851475143


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(number)
largest_prime_factor = max(pfs) # The largest element in the prime factor list
print(largest_prime_factor)
