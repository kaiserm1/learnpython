# -*- coding: utf-8 -*-
"""
    Created on Thu Mar 16 21:32:36 2017

    @author: maka_


    The following iterative sequence is defined for the set of positive integers:
    
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    
    Using the rule above and starting with 13, we generate the following sequence:
    
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    
    Which starting number, under one million, produces the longest chain?
    
    NOTE: Once the chain starts the terms are allowed to go above one million.
"""

cache_dict = {1:1}


def collatz_longest_chain(limit=1000000):
    """
    Input: limit as integer.
    :rtype: integer
    """
    for start_num in range(1, limit):
        sequence = 0
        num = start_num
        while num >= 1:
            if cache_dict.get(num) is None:
                if num % 2 == 0:
                    num /= 2
                else:
                    num *= 3
                    num += 1
                sequence += 1
            else:
                sequence += cache_dict.get(num)
                break
        cache_dict[start_num] = sequence
    return max(cache_dict, key=cache_dict.get)


print(collatz_longest_chain())