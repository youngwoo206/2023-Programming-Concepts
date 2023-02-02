'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''


def searchMatrix(matrix, target):

    for m in range(len(matrix)):
        L = 0
        R = len(matrix[0])-1

        while L <= R:
            mid = (L+R)//2

            if target > matrix[m][mid]:
                L = mid + 1
            elif target < matrix[m][mid]:
                R = mid - 1
            elif target == matrix[m][mid]:
                return True

    return False


searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
