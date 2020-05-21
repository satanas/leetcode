# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        paths = []
        self.traverse(paths, None, root)
        return paths
    
    def traverse(self, paths, prev_path, node):
        if node is None:
            return
        curr_path = self.new_path(prev_path, node.val)
        if node.left is None and node.right is None:
            paths.append(curr_path)
        else:
            if node.left is not None:
                self.traverse(paths, curr_path, node.left)
            if node.right is not None:
                self.traverse(paths, curr_path, node.right)

    def new_path(self, curr_path, val):
        return str(val) if curr_path is None else curr_path + "->" + str(val)

if __name__ == "__main__":
    fifthNode = TreeNode(5)
    ninethNode = TreeNode(9)
    seventhNode = TreeNode(7, ninethNode, None)
    secondNode = TreeNode(2, seventhNode, fifthNode)
    thirdNode = TreeNode(3)
    root = TreeNode(1, secondNode, thirdNode)

    s = Solution()
    print(s.binaryTreePaths(root))