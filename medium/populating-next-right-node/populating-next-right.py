"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if root is None:
            return None
        curr = root
        curr.next = None

        while curr is not None:
            parent = curr
            # connect all the children of parent
            while parent is not None:
                if parent.left is not None:
                    parent.left.next = parent.right
                    parent.right.next = self.get_next_right(parent)
                    parent = parent.next
                else:
                    parent = None
            
            curr = curr.left
        return root

    def get_next_right(self, node):
        if node.next is not None:
            return node.next.left
        return None

if __name__ == "__main__":
    s = Solution()
    s.connect([1,2,3,4,5,6,7])