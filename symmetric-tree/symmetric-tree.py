#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

#     1
#    / \
#   2   2
#  / \ / \
# 5  6 4  3

#     1
#    / \
#   2   2
#  / \ / \
# 5  4 4  

#     1
#    / \
#   3   2
#      / \
#     4  3

#     1
#    / \
#   2   2
#      / \
#     4  3

#         1
#        /\ 
#       /  \
#      /    \
#     2      2
#    /\      /\
#   /  \    /  \
#   5  4   4   5
#  /\  /\  /\  /\
# 6 7 8 9 9 8 7 5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.are_nodes_symmetric(root.left, root.right)

    def are_nodes_symmetric(self, node_a, node_b):
        if node_a is None and node_b is None:
            return True
        elif node_a is None or node_b is None:
            return False

        return node_a.val == node_b.val and \
            self.are_nodes_symmetric(node_a.left, node_b.right) and \
            self.are_nodes_symmetric(node_a.right, node_b.left)

if __name__ == "__main__":

#     1
#    / \
#   2   2
#      / \
#     4  3

    three = TreeNode(3)
    four = TreeNode(4)
    two1 = TreeNode(2, three, four)
    two2 = TreeNode(2, four, three)
    s = Solution()
    print(s.isSymmetric(TreeNode(1, two1, two2)))
    print(s.isSymmetric(None))

