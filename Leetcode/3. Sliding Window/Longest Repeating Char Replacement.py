'''
You are given a string s and an integer k. You can choose any character of the string and change it to any 
other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''


def characterReplacement(s, k):
    count = {}
    res = 0
    L = 0
    maxf = 0

    for R in range(len(s)):
        count[s[R]] = 1 + count.get(s[R], 0)
        maxf = max(maxf, count[s[R]])

        while (R-L+1) - maxf > k:
            count[s[L]] -= 1
            L += 1

        res = max(res, R-L+1)

    return res
