""" Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(range_start, range_end):
    result = 0
    for i in range(range_start, range_end+1):
        result += i ** 2
    return result

def square_of_sums(range_start, range_end):
    result_before_square = 0
    for i in range(range_start, range_end+1):
        result_before_square += i
    return result_before_square ** 2

def difference_between_both(result_sum, result_square):
    if result_sum>= result_square:
        result = result_sum - result_square
    else:
        result = result_square - result_sum
    return result


range_start = 1
range_end = 100

dif1 = sum_of_squares(range_start, range_end)
dif2 = square_of_sums(range_start, range_end)

print(difference_between_both(dif1, dif2))
