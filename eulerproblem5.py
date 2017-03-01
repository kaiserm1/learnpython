""" 2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
"""
import functools

def greatest_common_divisor(a, b):
    # Return greatest common divisor using Euclid's Algorithm.
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    # Return least common multiple.
    return a * b // greatest_common_divisor(a, b)


def lcmm(*args):
    # Return lcm of args.
    return functools.reduce(least_common_multiple, args)


print(lcmm(*range(1,20)))
