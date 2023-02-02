"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


def search(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (l + r)//2

        if nums[mid] > target:
            r = mid - 1

        elif nums[mid] < target:
            l = mid + 1

        elif nums[mid] == target:
            return mid

    return -1
