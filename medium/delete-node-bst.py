#         8
#       /   \
#      5     9
#     /  \     \
#    2    6     12
#   / \    \    / \
#  1   3    7  10 13

# key = 5

# Input: # [5,3,6,2,4,null,7]
# Key: 3
# Output: [5,4,6,2,null,null,7]

#         8
#       /   \
#      2     9
#     /  \     \
#    1    3     12
#          \    / \
#           6  10 13
#            \
#             7

#         8
#       /   \
#      2     9       
#     / \     \        
#    1   3     12       
#         \   /  \
#          6 10 13
#          \
#          7


#         8
#       /   \
#      6     9
#    /  \     \
#   5   7     12
#            / \
#           10 13
# key = 4

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

#     5
#    / \
#   4   6
#  /     \
# 2       7

#     1
#      \
#      2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://helloacm.com/how-to-delete-a-node-from-a-binary-search-tree/

class Solution:
    def deleteNode(self, node, key): # 2
        if node is None:
            return None

        if key > node.val:
            node.right = self.deleteNode(node.right, key)
        elif key < node.val:
            node.left = self.deleteNode(node.left, key)
        else:
            # case 1: no children
            if node.left is None and node.right is None:
                node = None
            # case 2: one child (left)
            elif node.left is not None and node.right is None:
                node = node.left
            # case 3: one child (right)
            elif node.left is None and node.right is not None:
                node = node.right
            # case 4: two children
            else:
                temp_right = node.right
                max_left = self.find_max_right_subtree(node.left)
                node = node.left
                max_left.right = temp_right

        return node

    def find_max_right_subtree(self, node):
        if node.right is None:
            return node
        else:
            return self.find_max_right_subtree(node.right)

def traverse_preorder(node, result):
    if node is not None:
        result.append(node.val)
        traverse_preorder(node.left, result)
        traverse_preorder(node.right, result)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    root = s.deleteNode(root, 3)
    result = []
    traverse_preorder(root, result)
    print(result)
    root = TreeNode(0)
    root = s.deleteNode(root, 0)
    result = []
    traverse_preorder(root, result)
    print(result)
    root = TreeNode(1, None, TreeNode(2))
    root = s.deleteNode(root, 1)
    result = []
    traverse_preorder(root, result)
    print(result)
    root = s.deleteNode(None, 0)
    result = []
    traverse_preorder(root, result)
    print(result)
    root = s.deleteNode(TreeNode(1, None, TreeNode(2)), 2)
    result = []
    traverse_preorder(root, result)
    print(result)
    root = s.deleteNode(TreeNode(2, TreeNode(1)), 2)
    result = []
    traverse_preorder(root, result)
    print(result)
