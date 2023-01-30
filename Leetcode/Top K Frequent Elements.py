"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""


def topKFrequent(nums, k):

    hashmap = {}
    output = []

    for num in nums:
        if num not in hashmap.keys():
            hashmap[num] = 1
        else:
            hashmap[num] += 1

    for i in range(k):
        maxKey = max(hashmap, key=hashmap.get)
        output.append(maxKey)
        del hashmap[maxKey]

    return output

# Time complexity: O(n+k)
# Space complexity: O(n)
