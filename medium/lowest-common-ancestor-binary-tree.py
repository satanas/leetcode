# For each node, we check if we can reach both nodes
# If true, then we store this as lowest ancestor and try with its children.
# If we cannot reach both nodes in a root node, then we return the curren lowest
# otherwise curr node will be lowest and we can try with its children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left is None and right is None:
            return None

        return left if left is not None else right
    
        