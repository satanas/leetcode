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

class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key and root.left is None and root.right is None:
            return None
        
        self.bst_deletion(None, root, key)
        return root

    def bst_deletion(self, prev, node, key):
        if node is None:
            return

        if node.val == key:
            if node.left is not None:
                temp_right = node.right
                self.copy_node(node.left, node)
                if prev is not None:
                    prev.left = node
                prev_node = node
                next_right = node.right
                while next_right is not None:
                    prev_node = next_right
                    next_right = prev_node.right
                prev_node.right = temp_right
            elif node.right is not None:
                self.copy_node(node.right, node)
            else:
                node = None
                if prev.val < key:
                    prev.right = None
                else:
                    prev.left = None
        else:
            if key < node.val:
                return self.bst_deletion(node, node.left, key)
            else:
                return self.bst_deletion(node, node.right, key)

    def copy_node(self, src_node, dst_node):
        dst_node.val = src_node.val
        dst_node.left = src_node.left
        dst_node.right = src_node.right

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
