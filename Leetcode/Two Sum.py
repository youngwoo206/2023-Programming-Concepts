'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''


def twoSum(nums, target):

    hashTable = {num: index for index, num in enumerate(nums)}
    print(hashTable)

    for i in range(len(nums)):

        target2 = target - nums[i]

        if target2 in hashTable:
            if i == hashTable[target2]:
                continue
            else:
                index_list = [i, hashTable[target2]]
                return sorted(index_list)

# time complexity: O(n)
# space complexity: O(n)


print(twoSum([3, 2, 4], 6))
