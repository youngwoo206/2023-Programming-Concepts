'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''


def longestConsecutive(nums):

    numSet = set(nums)
    sort = list(numSet)
    sort2 = sorted(sort)
    counter = 1
    maxCounter = 1

    if not nums:
        return 0

    for i in range(len(sort2)-1):
        if sort2[i+1] - sort2[i] == 1:
            counter += 1
            if counter > maxCounter:
                maxCounter = counter

        else:
            counter = 1

    return maxCounter
