'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


def containsDuplicate(nums):

    hashset = set()

    for n in nums:

        if n in hashset:
            return True
        else:
            hashset.add(n)

    return False

# Time complexity: O(n)
# Space complexity: O(n)
