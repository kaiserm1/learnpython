"""
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
"""
num = 2**1000
str_num = str(num)
num_sum = 0
for digit in str_num:
    num_sum += int(digit)

print(num_sum)