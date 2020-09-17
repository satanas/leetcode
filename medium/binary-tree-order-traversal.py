# Starting from the root
# Given a level, append all nodes in that level, from left to right to an array
# At the end of the level, append that array to the results

# We iterate all children from the node and append them to the queue
# We pop them from the queue to the array

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#     3
#    / \
#   9  20
#     /  \
#    15   7

# result = [[3], [9, 20], [15, 7]], queue = [], level = 2
# arr_level = [15, 7], node = 7

from collections import deque

class Solution:
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
            
        queue = deque()
        queue.append(root)
        
        while queue:
            level = len(queue)
            arr_level = []
            for i in range(level):
                node = queue.popleft()
                arr_level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(arr_level)
        return result
            

if __name__ == "__main__":
    s = Solution()
    print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.levelOrder(None))