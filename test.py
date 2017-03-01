import math

number = 300425737531

def is_prime(n):
    # is_prime is usually slower than sieve
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True



def primeSieve(sieveSize):
     # Returns a list of prime numbers calculated using
     # the Sieve of Eratosthenes algorithm.

     sieve = [True] * sieveSize
     sieve[0] = False # zero and one are not prime numbers
     sieve[1] = False

     # create the sieve
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i

     # compile the list of primes
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)

     return primes
