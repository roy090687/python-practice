"""
Module: smallest_missing_positive
---------------------------------
This module provides a function to find the smallest missing positive integer
from a given list of integers.
Example:
Input: [1, 3, 6, 4, 1, 2]
Output: 5
"""

def missing_smallest_integer(input):
    input.sort()
    smallest = 1
    for num in input:
        if num == smallest:
            smallest += 1
    return smallest

list1 = [1, 2, 3, 4, 6]
list2 = [1, 2, 3]
list3 = [1, 3, 6, 4, 1, 2]

print("Missing smallest integer-1:", missing_smallest_integer(list1))
print("Missing smallest integer-2:", missing_smallest_integer(list2))
print("Missing smallest integer-3:", missing_smallest_integer(list3))
