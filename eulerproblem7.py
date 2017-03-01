""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
"""

import math

number = 300425737531
final_prime = 6

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def generate_primes(number_of_primes):
    # Generate prime numbers until number_of_primes is reached
    counter = 0
    num = 0
    while True:
        if counter <= number_of_primes:
            if is_prime(num):
                counter += 1
            num += 1
        else:
            break
    print(num, counter)
    return counter


print(generate_primes(final_prime))
