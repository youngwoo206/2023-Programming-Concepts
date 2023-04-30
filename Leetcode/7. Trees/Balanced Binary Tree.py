'''
Given a binary tree, determine if it's height balanced
'''


def isBalanced(root):

    # recursive function starting from bottom, returns [balanced? (bool) and height (int)]
    def dfs(root):
        # check if node is null
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        height = 1 + max(left[1], right[1])

        return [balanced, height]

    return dfs(root)[0]
