""" Largest Palindrome product: Find the largest palindrome made
    from the product of two 3-digit numbers.

    A palindromic number reads the same both ways. The largest palindrome
    made from the product of 2-digit numbers is 9009 = 91 x 99.
"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def palindrome_factors(num1, num2):
    palindromes = []
    for i in num1:
        for j in num2:
            candidate = i * j
            if is_palindrome(candidate):
                palindromes.append(candidate)
    return palindromes


def create_num_list(range_start, range_end):
    num_list = []
    for i in range(range_start, range_end+1):
        num_list.append(i)
    return num_list


num_list_1 = create_num_list(100, 999)
num_list_2 = create_num_list(100, 999)

print(max(palindrome_factors(num_list_1, num_list_2)))
