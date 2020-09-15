#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]

# left, Root, right
# Traverse the left subtree
# Visit root
# Traverse the right subtree

# Iterative approach:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        path = []
        visited = []
        stack = []
        stack.insert(0, root)

        if root is None:
            return path

        while len(stack) > 0:
            node = stack.pop(0)
            if node not in visited:
                visited.append(node)
                if node.left is not None:
                    stack.insert(0, node)
                    stack.insert(0, node.left)
                else:
                    path.append(node.val)
                    if node.right is not None:
                        stack.insert(0, node.right)
            else:
                path.append(node.val)
                if node.right is not None:
                    stack.insert(0, node.right)


# node = 2
# visited = 1, 3, 4, 5, 2, 7
# path = [4, 3, 5, 1, 7, 2]
# stack = 