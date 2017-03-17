""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

import math


def prime_sieve(sieve_size):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieve_size
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(sieve_size):
        if sieve[i] == True:
            primes.append(i)

    return primes


def sum_of_primes(primes_list):
    result = 0
    for i in primes_list:
        result += i
    return result


limit = 2000000

list_of_primes = prime_sieve(limit)

print(sum(list_of_primes))
print(sum_of_primes(list_of_primes))
