'''
Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''


def subsets(nums):
    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # include nums[i] (left path)
        subset.append(nums[i])
        dfs(i + 1)

        # dont include nums[1] (right path)
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return res
