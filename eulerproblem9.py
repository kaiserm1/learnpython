""" A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which,

    a2 + b2 = c2

    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

target = 1000

def pyt_triplet(num):
    for i in range(1, num, 1):
        for j in range(1, num - 1, 1):
            k = num - i - j
            if i**2 + j**2 == k**2:
                return i * j * k
    return 0

print(pyt_triplet(target))
