# What is the largest prime factor of the number 600851475143?
import math

number = 600851475143
prime_factor_list = 0


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


def max_prime_factor(l):
    for m in range(int(l/2),0):
        if is_prime(m):
            print(m)
    return m

for m in range(0,int(number/2),-1):
    if is_prime(m):
        print(m)
