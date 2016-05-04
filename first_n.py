#!/usr/bin/env python


def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1

    # Returns a list of the first n numbers
    return nums

# This won't work for very large numbers, since it keeps the list of all these integers in memory
sum_of_first_n = sum(firstn(1000000))
