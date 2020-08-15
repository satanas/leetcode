# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    hashmap = {}
    pre_index = 0

    def buildTree(self, preorder, inorder):
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i
        return self.build(preorder, inorder, 0, len(inorder) - 1)

    def build(self, preorder, inorder, start, end):
        if start > end:
            return None
        
        curr = preorder[self.pre_index]
        self.pre_index += 1
        root = TreeNode(curr)
        if start == end:
            return root
        
        root.left = self.build(preorder, inorder, start, self.hashmap[curr] - 1)
        root.right = self.build(preorder, inorder, self.hashmap[curr] + 1, end)

        return root


if __name__ == "__main__":
    s = Solution()
    s.buildTree([3,9,20,15,7], [9,3,15,20,7])