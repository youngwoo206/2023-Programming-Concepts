'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''


def productExceptSelf(nums):

    cur1 = 1
    cur2 = 1
    prod1 = []
    prod2 = [1 for i in nums]

    for i in range(len(nums)):
        if i == 0:
            prod1.append(1)

        else:
            cur1 = cur1*nums[i-1]
            prod1.append(cur1)

    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            continue
        else:
            cur2 = cur2*nums[i+1]
            prod2[i] = cur2

    print(prod1, prod2)

    output = [prod1[i]*prod2[i] for i in range(len(prod1))]

    return output
