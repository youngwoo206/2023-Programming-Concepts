'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered 
from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''


def plusOne(digits):

    length = len(digits) - 1

    while digits[length] == 9:
        digits[length] = 0
        length -= 1

    if (length < 0):
        digits = [1] + digits

    else:
        digits[length] += 1

    return digits


plusOne([1, 2, 3])
