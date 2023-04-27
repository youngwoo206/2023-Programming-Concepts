'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''


def isSameTree(p, q):
    p_vals = []
    q_vals = []

    def preorder_dfs(start, traversal):
        if start:
            traversal.append(start.val)
            if start.left:
                traversal = preorder_dfs(start.left, traversal)
            else:
                traversal.append('null')
            if start.right:
                traversal = preorder_dfs(start.right, traversal)
            else:
                traversal.append('null')
        return traversal

    preorder_dfs(p, p_vals)
    preorder_dfs(q, q_vals)

    if p_vals == q_vals:
        return True
    else:
        return False
