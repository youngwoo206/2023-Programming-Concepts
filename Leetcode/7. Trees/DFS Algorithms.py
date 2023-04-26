class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # Pre-order DFS:
    def preorder_dfs(self, start, traversal):
        # root -> left -> right
        if start:
            traversal += (str(start.value) + "-")  # root
            traversal = self.preorder_dfs(start.left, traversal)  # left
            traversal = self.preorder_dfs(start.right, traversal)  # right

        return traversal

    # In-order DFS:
    def inorder_dfs(self, start, traversal):
        # left -> root -> right
        if start:
            traversal = self.inorder_dfs(start.left, traversal)  # left
            traversal += (str(start.value) + "-")  # root
            traversal = self.inorder_dfs(start.right, traversal)  # right

        return traversal

    # Post-order DFS:
    def postorder_dfs(self, start, traversal):
        # left -> right -> root
        if start:
            traversal = self.postorder_dfs(start.left, traversal)  # left
            traversal = self.postorder_dfs(start.right, traversal)  # right
            traversal += (str(start.value) + "-")  # root

        return traversal
