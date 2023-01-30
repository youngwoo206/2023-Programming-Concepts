'''
Given a non-negative integer x, return the square root of x rounded down to 
the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
'''
# solve by using binary search


def mySqrt(x):

    left, right = 0, x

    while left <= right:

        mid = (left + right)//2

        if mid*mid > x:

            right = mid - 1

        elif mid*mid < x:

            left = mid + 1

        else:
            return mid

    return right
